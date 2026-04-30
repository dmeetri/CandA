import os
import uuid

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import FileModel


@receiver(pre_save, sender=FileModel)
def rename_file_before_save(sender, instance, **kwargs):
    if instance.file:
        old_file = instance.file
        ext_with_dot = os.path.splitext(old_file.name)[1]
        ext_without_dot = ext_with_dot[1:] if ext_with_dot.startswith('.') else ext_with_dot

        instance.extension = ext_without_dot.upper()

        new_filename = f"{uuid.uuid4().hex}{ext_with_dot}"
        instance.file.name = new_filename
