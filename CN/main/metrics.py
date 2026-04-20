import shutil

from .services import send_email_message
from django.conf import settings
from django.http import JsonResponse

def send_warning(message):
    result = send_email_message(
        to_email=settings.EMAIL_FOR_SEND,
        subject='C&A WARNING',
        message=message
    )
    return JsonResponse(result)

def get_disk_usega(path='/'):
    send_warning('ntcn')

    total, used, free = shutil.disk_usage(path)

    to_gb = 2**32
    return {
        "total": total / to_gb,
        "used": used / to_gb,
        "free": free / to_gb,
        "percent_used": (used / total) * 100
    }
