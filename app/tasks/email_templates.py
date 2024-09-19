from email.message import EmailMessage
from app.config import settings

def create_random_password_template(user_email: str,
                                    random_password: str):
    email = EmailMessage()

    email['Subject'] = 'New password'
    email['From'] = settings.SMTP_USER
    email['To'] = user_email

    email.set_content(
        f'''
            <h1>Your password is <b>{random_password}<b><h1>
        ''',
        subtype = 'html'
    )
    return email