from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings

from . import models, forms, metrics

def home(request):
    return render(request, 'base.html')

# FILES

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
        context['disk_usage'] = metrics.get_disk_usega()

        return context


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

# EMAIL SEND

def my_view(request):
    try:
        send_mail(
            subject='Внимание! Заполнение диска на сервере',
            message=f'Диск заполнен на 90%. Срочно примите меры.',
            from_email=None,
            recipient_list=[
                settings.EMAIL_FOR_SEND
            ],
            fail_silently=False,
        )
        print("Письмо успешно отправлено!")
    except Exception as e:
        print(f"Произошла ошибка при отправке письма: {e}")

    return render(request, 'base.html')
