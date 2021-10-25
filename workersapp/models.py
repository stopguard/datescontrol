from django.db import models


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

    @property
    def status(self):
        items = self.itemmodel_set.filter(is_active=True)
        result = 0
        for item in items:
            status = item.status
            if status > result:
                result = status
                if result == 3:
                    break
        return result

    @property
    def brig_status(self):
        if self.is_brig:
            workers = WorkerModel.objects.filter(departament=self.departament, brig=self, is_active=True)
            result = 0
            for worker in workers:
                status = worker.status
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
