from django import forms
from django.contrib.auth.models import Group

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
            'extension',
        ]


class FilterFilesForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Поиск'})
    )
    extension = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Все'),
            ('VIDEO', 'Видео'),
            ('PNG', 'png'),
            ('JPEG', 'jpeg'),
            ('WEB', 'web'),
            ('TXT', 'Текст'),
            ('PDF', 'pdf'),
            ('WORD', 'Word'),
            ('EXCEL', 'Excel'),
            ('ARCHIVE', 'Архив'),
            ('OTHER', 'Другое'),
        ]
    )
