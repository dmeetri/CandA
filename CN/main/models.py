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


class FileModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='files/')
    extension = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
