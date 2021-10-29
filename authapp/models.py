from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    photo = models.ImageField('Фото', upload_to='photo', blank=True)
    full_name = models.CharField('ФИО', max_length=256, default='')
    telegram_id = models.IntegerField('Telegram ID', default=0)
    phones = models.TextField('Телефоны', blank=True)