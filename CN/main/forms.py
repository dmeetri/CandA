from django import forms
from . import models

# === FILES ===

class CreateFileForm(forms.ModelForm):
    title = forms.CharField(
        required=False,
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
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Название'})
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Описание'})
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
