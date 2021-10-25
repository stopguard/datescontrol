from django.db import models
from datetime import date, datetime
from calendar import monthrange


# Create your models here.
class CityModel(models.Model):
    name = models.CharField('Филиал', max_length=256)
    description = models.TextField('Примечание', blank=True)
    photo = models.ImageField('Фото', upload_to='city_images', blank=True)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'
        ordering = ['name']


class CompanyModel(models.Model):
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    name = models.CharField('Организация', max_length=256)
    description = models.TextField('Примечание', blank=True)
    photo = models.ImageField('Фото', upload_to='company_images', blank=True)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.name} ({self.city.name})'

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name']


class DepartamentModel(models.Model):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    name = models.CharField('Подразделение', max_length=256)
    description = models.TextField('Примечание', blank=True)
    photo = models.ImageField('Фото', upload_to='departament_images', blank=True)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.name} ({self.company.name}-{self.company.city.name})'

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['name']


class WorkerModel(models.Model):
    departament = models.ForeignKey(DepartamentModel, on_delete=models.CASCADE)
    name = models.CharField('ФИО сотрудника', max_length=256)
    number = models.IntegerField('Табельный номер', default=0)
    description = models.TextField('Примечание', blank=True)
    photo = models.ImageField('Фото', upload_to='photo', blank=True)
    is_brig = models.BooleanField('Бригадир', default=False)
    brig = models.ForeignKey('self',
                             on_delete=models.PROTECT,
                             limit_choices_to={'is_brig': True},
                             blank=True, null=True)
    is_company_leader = models.BooleanField('Руководитель орг.', default=False)
    is_departament_leader = models.BooleanField('Руководитель подр.', default=False)
    telegram_id = models.IntegerField('Telegram ID', default=0)
    email = models.EmailField('Email', blank=True)
    phones = models.TextField('Телефоны', blank=True)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.name} ({self.departament.name}-{self.departament.company.name})'

    def status(self):
        items = self.itemmodel_set.filter(is_active=True)
        result = 0
        for item in items:
            status = item.status()
            if status > result:
                result = status
                if result == 3:
                    break
        return result

    def brig_status(self):
        if self.is_brig:
            workers = WorkerModel.objects.filter(departament=self.departament, brig=self, is_active=True)
            result = 0
            for worker in workers:
                status = worker.status()
                if status > result:
                    result = status
                    if result == 3:
                        break
            return result
        return 0

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name']


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


class ItemModel(models.Model):
    worker = models.ForeignKey(WorkerModel, on_delete=models.CASCADE)
    item_type = models.ForeignKey(ItemTypeModel, on_delete=models.CASCADE)
    description = models.TextField('Примечание', blank=True)
    inventory_number = models.CharField('Инвентарный номер', max_length=64, blank=True)
    change_for = models.DateField('Дата выдачи', blank=True)
    test_for = models.DateField('Дата проверки')
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.item_type.name}-{self.inventory_number} ({self.worker.name})'

    def test_to(self):
        return add_months(self.test_for, self.item_type.test_interval)

    def change_to(self):
        return add_months(self.change_for, self.item_type.change_interval)

    def elapse(self):
        is_doc = self.item_type.group.doc_or_tool == 'Удостоверение'
        return min(self.test_to(), self.change_to()) if is_doc else self.test_to()

    def delta(self):
        next_test = self.elapse()
        today = datetime.now()
        today = date(today.year, today.month, today.day)
        return (next_test - today).days

    def status(self):
        delta = self.delta()
        if delta > 90:
            return 0
        elif delta > 30:
            return 1
        elif delta > 0:
            return 2
        else:
            return 3

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['worker']


def add_months(source_date, months):
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, monthrange(year, month)[1])
    return date(year, month, day)
