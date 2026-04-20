from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(
        unique=True,
        max_length=100,
        blank=False, null=False,
    )

    email = models.CharField(
        max_length=200,
        unique=True,
        blank=False, null=False,
    )
    email_confirmed = models.BooleanField(default=False)

    USER_ROLES = (
        ('FULLADMIN', 'Гл.Админ'),
        ('ADMIN', 'Админ'),
        ('USER', 'Пользователь'),
        ('VIEWER', 'Наблюдатель'),
    )
    roles = models.CharField(
        choices=USER_ROLES,
        default='VIEWER',
    )


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
        choices=FILE_EXTENSION,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
