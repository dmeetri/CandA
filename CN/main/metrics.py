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

    return {
        "total": total / 1073741824,
        "used": used / 1073741824,
        "free": free / 1073741824,
        "percent_used": (used / total) * 100,
    }
