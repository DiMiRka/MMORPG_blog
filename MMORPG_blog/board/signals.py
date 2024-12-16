from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import send_mail
from board.models import *
from account.models import *
from account.views import generate_string
from django.conf import settings
from django.contrib.auth import get_user_model

