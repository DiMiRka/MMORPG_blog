from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from board.models import *
from account.models import *
from account.views import generate_string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from MMORPG_blog import settings


@receiver(post_save, sender=get_user_model(), )
def new_user_code(sender, instance, created, **kwargs):
    if created:
        new_code = OneTimeCode.objects.create(user=instance,
                                      code=generate_string(6))
        new_code.save()

        message = f'Ваш код авторизации на форуме: \n' \
                  f'{new_code.code}'
        send_mail(
            f'Код авторизации пользователя',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
        )


@receiver(post_save, sender=PostsResponses, )
def notify_author_new_reply(sender, instance, created, **kwargs):
    if created:
        html_content = render_to_string(
            'account/appointment_created.html',
            {
                'link': f'{settings.SITE_URL}/account/',
                'name': instance.post.author,
                'post': instance.post.name
            }
        )

        msg = EmailMultiAlternatives(
            subject='Новый отклик к вашему посту!',
            body='',
            from_email=settings.EMAIL_ADMIN,
            to=[instance.post.author.email]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
