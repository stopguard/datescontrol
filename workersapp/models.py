from django.contrib.auth import get_user_model
from django.db import models


class CityModel(models.Model):
    name = models.CharField('Филиал', max_length=256)
    description = models.TextField('Примечание', blank=True)
    photo = models.ImageField('Фото', upload_to='city_images', blank=True)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.name}'

    def workers(self, brig_only=False):
        companies = self.companymodel_set.filter(is_active=True)
        departaments = DepartamentModel.objects.filter(company__in=companies, is_active=True)
        return WorkerModel.objects.filter(departament__in=departaments, is_brig=True, is_active=True) \
            if brig_only \
            else WorkerModel.objects.filter(departament__in=departaments, is_active=True)

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

    def workers(self, brig_only=False):
        departaments = self.departamentmodel_set.filter(is_active=True)
        return WorkerModel.objects.filter(departament__in=departaments, is_brig=True, is_active=True) \
            if brig_only \
            else WorkerModel.objects.filter(departament__in=departaments, is_active=True)

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

    def workers(self, brig_only=False):
        return self.workermodel_set.filter(is_brig=True, is_active=True) \
            if brig_only \
            else self.workermodel_set.filter(is_active=True)

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        ordering = ['name']


class WorkerModel(models.Model):
    departament = models.ForeignKey(DepartamentModel, on_delete=models.CASCADE)
    linked_user = models.ForeignKey(get_user_model(),
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True)
    brig = models.ForeignKey('self',
                             on_delete=models.PROTECT,
                             limit_choices_to={'is_brig': True},
                             blank=True, null=True)
    name = models.CharField('ФИО сотрудника', max_length=256)
    number = models.IntegerField('Табельный номер', default=0)
    description = models.TextField('Примечание', blank=True)
    is_brig = models.BooleanField('Бригадир', default=False)
    is_company_leader = models.BooleanField('Руководитель орг.', default=False)
    is_departament_leader = models.BooleanField('Руководитель подр.', default=False)
    is_active = models.BooleanField('Активен', default=True)

    def __str__(self):
        return f'{self.name} ({self.departament.name}-{self.departament.company.city.name})'

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
            workers = self.workermodel_set.filter(is_active=True)
            result = 0
            for worker in workers:
                status = worker.status
                if status > result:
                    result = status
                    if result == 3:
                        break
            return result
        return 0

    @property
    def tools(self):
        tools_set = self.itemmodel_set.filter(item_type__group__doc_or_tool='Инструмент', is_active=True)
        return sorted(tools_set, reverse=True, key=lambda itm: itm.status)

    @property
    def docs(self):
        docs_set = self.itemmodel_set.filter(item_type__group__doc_or_tool='Удостоверение', is_active=True)
        return sorted(docs_set, reverse=True, key=lambda itm: itm.status)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name']
