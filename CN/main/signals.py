import os
import uuid

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import FileModel

@receiver(pre_save, sender=FileModel)
def rename_file_before_save(sender, instance, **kwargs):
    if instance.file:
        old_file = instance.file
        ext = os.path.splitext(old_file.name)[1]

        new_filename = f"{uuid.uuid4().hex}{ext}"
        instance.file.name = new_filename
