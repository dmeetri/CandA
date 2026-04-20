import shutil

from .services import send_email_message
from django.conf import settings

def get_disk_usega(path='/'):
    '''
    result = send_email_message(
        to_email=settings.EMAIL_FOR_SEND,
        subject='C&A WARNING',
        message="efnjn"
    )
    '''

    total, used, free = shutil.disk_usage(path)

    to_gb = 2**32
    return {
        "total": total / to_gb,
        "used": used / to_gb,
        "free": free / to_gb,
        "percent_used": (used / total) * 100
    }
