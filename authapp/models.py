from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    photo = models.ImageField('Фото', upload_to='photo', blank=True)
    full_name = models.CharField('ФИО', max_length=256, default='')
    number = models.IntegerField('Табельный номер', default=0)
    telegram_id = models.IntegerField('Telegram ID', null=True)
