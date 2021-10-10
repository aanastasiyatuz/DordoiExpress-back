from celery import shared_task
from django.core.mail import send_mail
from decouple import config

domain = config("DOMAIN")

@shared_task
def send_activation_mail(email, activation_code):
    print(domain)
    activation_url = f'{domain}/account/activate/{activation_code}'
    message = f"""Чтобы активировать свой аккаунт, перейдите по ссылке: {activation_url}"""
    send_mail(
        'Активация аккаунта',
        message,
        'dordoiExpress@gmail.com',
        [email, ],
    )


@shared_task
def send_activation_code(email, activation_code):
    activation_url = f'{domain}/account/forgot-password-complete/{activation_code}'
    message = f"""Чтобы восстановить пароль, пройдите по данной ссылке: {activation_url}"""
    send_mail(
        'Восстановление пароля',
        message,
        'dordoiExpress@gmail.com',
        [email, ],
    )