import shutil

from PIL import Image

from django.core.mail import send_mail
from django.conf import settings

# === EMAIL ===

def send_email_message(to_email, subject, message):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=None,
            recipient_list=[to_email],
            fail_silently=False,
        )
        return {
            'success': True,
            'message': f'Письмо отправлено на {to_email}!'
        }
    except Exception as e:
        return {
            'success': False,
            'error': f'Ошибка при отправке: {str(e)}'
        }

# === SYSTEM METRICS ===

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

# === IMAGES ===

class ImageConverter:
    def __init__(self) -> None:
        self.images = []

    def load_images(self, images):
        pass



