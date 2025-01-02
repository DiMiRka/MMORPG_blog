import datetime
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from MMORPG_blog import settings
from .models import Post, User


def send(posts_send, user, mail):
    html_content = render_to_string(
        'send_every_week.html',
        {
            'name': user,
            'posts': posts_send
        }
    )

    msg = EmailMultiAlternatives(
        subject='Новые посты за прошедшую неделю!',
        body='',
        from_email=settings.EMAIL_ADMIN,
        to=[mail]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def send_mails():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_in__gte=last_week)
    post_info = {}
    print('------------------------')
    print(posts)
    print('------------------------')
    for p in posts:
        post_info[p.pk] = p.name
    for s in User.objects.all():
        name = s.username
        mail = s.email
        send(posts_send=post_info, user=name, mail=mail)
