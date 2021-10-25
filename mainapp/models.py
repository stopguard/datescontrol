from datetime import date, datetime
from calendar import monthrange

from django.db import models

from itemtypesapp.models import ItemTypeModel
from workersapp.models import WorkerModel


# Create your models here.
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

    @property
    def test_to(self):
        return add_months(self.test_for, self.item_type.test_interval)

    @property
    def change_to(self):
        return add_months(self.change_for, self.item_type.change_interval)

    @property
    def elapse(self):
        is_doc = self.item_type.group.doc_or_tool == 'Удостоверение'
        return min(self.test_to, self.change_to) if is_doc else self.test_to

    @property
    def delta(self):
        next_test = self.elapse
        today = datetime.now()
        today = date(today.year, today.month, today.day)
        return (next_test - today).days

    @property
    def status(self):
        delta = self.delta
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
