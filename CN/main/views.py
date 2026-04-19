from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy

from . import models, forms

class FileCreateView(CreateView):
    model = models.FileModel
    form_class = forms.CreateFileForm
    template_name = 'files/create_file.html'
    success_url = reverse_lazy('files')


class FilesListView(ListView):
    model = models.FileModel
    template_name = 'files/files.html'
    context_object_name = 'files'
