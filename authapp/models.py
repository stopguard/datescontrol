from django.contrib.auth.models import AbstractUser
from django.db import models

from workersapp.models import WorkerModel


# Create your models here.
class CustomUser(AbstractUser):
    photo = models.ImageField('Фото', upload_to='photo', blank=True)
    full_name = models.CharField('ФИО', max_length=256, default='')
    linked_worker = models.ForeignKey(WorkerModel, on_delete=models.SET_NULL, blank=True, null=True)
