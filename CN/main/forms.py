from django import forms
from . import models

class CreateFileForm(forms.ModelForm):
    class Meta:
        model = models.FileModel
        fields = [
            'title',
            'description',
            'file',
            'extension',
        ]
