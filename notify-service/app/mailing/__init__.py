__all__ = [
    "send_welcome_email",
    "send_login_email",
    "send_few_trainings_mail_notification",
]


from .login import send_login_email
from .trainings import send_few_trainings_mail_notification
from .welcome import send_welcome_email
