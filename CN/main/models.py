from django.db import models

class FileModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='files/')

    FILE_EXTENSION = (
        ('VIDEO', 'Видео'),
        ('IMAGE', 'Картинка'),
        ('TXT', 'Текст'),
        ('PDF', 'pdf'),
        ('WORD', 'Word'),
        ('EXCEL', 'Excel'),
        ('OTHER', 'Другое'),
    )
    extension = models.CharField(
        max_length=10,
        choices=FILE_EXTENSION
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)