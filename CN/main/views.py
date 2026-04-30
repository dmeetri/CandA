import json

from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.views.decorators.cache import cache_page
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib import messages

from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.shortcuts import redirect

from .services import send_email_message

from . import models, forms

# === GROUPS ===

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = forms.CreateGroupFrom
    template_name = 'registration/groups/create_group.html'
    success_url = reverse_lazy('groupslist')


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'registration/groups/groups.html'
    context_object_name = 'groups'


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('groupslist')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# === USERS ===

User = get_user_model()

@method_decorator(cache_page(60 * 15), name='dispatch')
class UsersListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'registration/users.html'
    context_object_name = 'users'
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().only('id', 'username', 'email')


class UsersDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/profile.html'
    context_object_name = 'duser'


# === FILES ===

class FileCreateView(LoginRequiredMixin, CreateView):
    model = models.FileModel
    form_class = forms.CreateFileForm
    template_name = 'files/create_file.html'
    success_url = reverse_lazy('fileslist')


@method_decorator(cache_page(60 * 15), name='dispatch')
class FilesListView(LoginRequiredMixin, ListView):
    model = models.FileModel
    template_name = 'files/files.html'
    context_object_name = 'files'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = forms.FilterFilesForm(self.request.GET)

        latest_file = models.FileModel.objects.order_by('-updated_at').first()
        if latest_file: context['last_update_date'] = latest_file.updated_at
        else: context['last_update_date'] = None

        return context

    def get_queryset(self):
        queryset = super().get_queryset().only(
            'id', 'title', 'description', 'extension', 'created_at', 'updated_at'
        ).order_by('-updated_at')

        search_query = self.request.GET.get('search')
        extension = self.request.GET.get('extension')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        if extension:
            queryset = queryset.filter(extension=extension)

        return queryset


class FileDetailView(LoginRequiredMixin, DetailView):
    model = models.FileModel
    template_name = 'files/file.html'
    context_object_name = 'file'


class FileUpdateView(LoginRequiredMixin, UpdateView):
    model = models.FileModel
    form_class = forms.CreateFileForm
    template_name = 'files/file.html'
    success_url = reverse_lazy('filesdetail')


class FilesDeleteSelectedView(LoginRequiredMixin, View):
    success_url = reverse_lazy('fileslist')

    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('selected_items')

        if not selected_ids:
            messages.error(request, 'Не выбрано ни одного элемента для удаления')
            return redirect(self.success_url)

        valid_ids = [id for id in selected_ids if id.isdigit()]
        if not valid_ids:
            messages.error(request, 'Выбраны некорректные элементы')
            return redirect(self.success_url)

        deleted_count, _ = models.FileModel.objects.filter(id__in=valid_ids).delete()
        if deleted_count:
            messages.success(request, f'Успешно удалено {deleted_count} записей')
        else:
            messages.error(request, 'Не удалось удалить выбранные записи')

        return redirect(self.success_url)


class FileDeleteView(LoginRequiredMixin, DeleteView):
    model = models.FileModel
    success_url = reverse_lazy('fileslist')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# === EMAIL SEND ===

def send_email(request):
    try:
        data = json.loads(request.body)

        result = send_email_message(
            to_email=data.get('to'),
            subject=data.get('subject', 'Нет темы'),
            message=data.get('message', '')
        )

        if result['success']:
            return JsonResponse(result, status=200)
        else:
            return JsonResponse(result, status=500)
    except json.JSONDecodeError:
        return JsonResponse({
            'error': 'Неверный JSON формат'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'error': f'Ошибка при отправке: {str(e)}'
        }, status=500)
