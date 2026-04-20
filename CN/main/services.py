from django.core.mail import send_mail

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
