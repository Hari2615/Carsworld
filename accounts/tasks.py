from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
from celery import shared_task
logger = get_task_logger(__name__)

@shared_task
def send_email(subject,body,from_email,to,reply_to):
    email = EmailMessage(
        
                subject=subject,
                body=body,
                from_email=from_email,
                to=to,
                reply_to=reply_to,
            )
    
    email.send(fail_silently=False)
    return 'Email Sent'
  
