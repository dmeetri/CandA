import json

from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse

from .services import send_email_message

from . import models, forms

def home(request):
    return render(request, 'base.html')

# === USERS ===

class ProfileView(DetailView):
    model = User
    template_name = 'registration/profile.html'
    context_object_name = 'user'

# === FILES ===

class FileCreateView(CreateView):
    model = models.FileModel
    form_class = forms.CreateFileForm
    template_name = 'files/create_file.html'
    success_url = reverse_lazy('fileslist')


class FilesListView(LoginRequiredMixin, ListView):
    model = models.FileModel
    template_name = 'files/files.html'
    context_object_name = 'files'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = forms.FilterFilesForm(self.request.GET)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        description = self.request.GET.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        extension = self.request.GET.get('extension')
        if extension:
            queryset = queryset.filter(extension__icontains=extension)

        return queryset


class FileDetailView(DetailView):
    model = models.FileModel
    template_name = 'files/file.html'
    context_object_name = 'file'


class FileUpdateView(UpdateView):
    model = models.FileModel
    form_class = forms.CreateFileForm
    template_name = 'files/file.html'
    success_url = reverse_lazy('filesdetail')


class FileDeleteView(DeleteView):
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
