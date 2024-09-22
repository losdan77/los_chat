import smtplib
from app.config import settings
from app.tasks.celery_app import celery
from app.tasks.email_templates import create_random_password_template

@celery.task
def send_password_email(user_email: str,
                        random_password: str,):
    msg_content = create_random_password_template(user_email,
                                                  random_password)

    with smtplib.SMTP(settings.SMTP_HOST, int(settings.SMTP_PORT)) as server:
        server.set_debuglevel(1) 
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
