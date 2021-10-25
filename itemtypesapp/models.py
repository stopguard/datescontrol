from django.db import models


# Create your models here.
class ItemGroupModel(models.Model):
    TOOL = 'Инструмент'
    DOC = 'Удостоверение'
    DOC_OR_TOOL_CHOICES = [
        (TOOL, 'Инструмент'),
        (DOC, 'Удостоверение'),
    ]
    name = models.CharField('Группа предметов', max_length=256)
    description = models.TextField('Примечание', blank=True)
    doc_or_tool = models.CharField('Тип предмета', max_length=64, choices=DOC_OR_TOOL_CHOICES)
    photo = models.ImageField('Фото', upload_to='item_group_images', blank=True)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.name} ({self.doc_or_tool})'

    class Meta:
        verbose_name = 'Группа предметов'
        verbose_name_plural = 'Группы предметов'
        ordering = ['name']


class ItemTypeModel(models.Model):
    group = models.ForeignKey(ItemGroupModel, on_delete=models.CASCADE)
    name = models.CharField('Имя предмета', max_length=256)
    description = models.TextField('Примечание', blank=True)
    photo = models.ImageField('Фото', upload_to='item_images', blank=True)
    change_interval = models.SmallIntegerField('Интервал выдачи', default=12)
    test_interval = models.SmallIntegerField('Интервал проверки', default=12)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.name} ({self.group.doc_or_tool})'

    class Meta:
        verbose_name = 'Тип предмета'
        verbose_name_plural = 'Типы предметов'
        ordering = ['name']
