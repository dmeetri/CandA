from django import forms
from django.contrib.auth.models import Group
from django.core.cache import cache

from . import models

# === GROUPS ===

class CreateGroupFrom(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

# === FILES ===

class CreateFileForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Название'})
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Описание'})
    )

    class Meta:
        model = models.FileModel
        fields = [
            'title',
            'description',
            'file',
        ]


class FilterFilesForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Поиск'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['extension'] = forms.ChoiceField(
            required=False,
            choices=self.get_extension_choices(),
            widget=forms.Select(attrs={'class': 'form-control'})
        )

    def get_extension_choices(self):
        cache_key = 'file_extensions_choices'
        choices = cache.get(cache_key)

        if choices is None:
            extensions = models.FileModel.objects.exclude(
                extension=''
            ).exclude(
                extension__isnull=True
            ).values_list(
                'extension', flat=True
            ).distinct().order_by('extension')

            choices = [('', 'Все')]
            extension_names = {
                'VIDEO': 'Видео',
                'PNG': 'PNG',
                'JPEG': 'JPEG',
                'JPG': 'JPG',
                'WEB': 'WEB',
                'TXT': 'Текст',
                'PDF': 'PDF',
                'DOC': 'Word',
                'DOCX': 'Word',
                'XLS': 'Excel',
                'XLSX': 'Excel',
                'ZIP': 'Архив',
                'RAR': 'Архив',
                'GZ': 'Архив',
                'MP4': 'Видео',
                'AVI': 'Видео',
                'MOV': 'Видео',
                'MKV': 'Видео',
                'MP3': 'Аудио',
                'WAV': 'Аудио',
            }

            for ext in extensions:
                display_name = extension_names.get(ext, ext)
                choices.append((ext, display_name))

            cache.set(cache_key, choices, 3600)

        return choices
