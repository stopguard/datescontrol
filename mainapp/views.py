from datetime import date, timedelta, datetime

from django.shortcuts import render

from mainapp.models import ItemModel
from itemtypesapp.models import ItemTypeModel
from workersapp.models import CityModel, CompanyModel, DepartamentModel, WorkerModel


# Create your views here.
def index(request):
    context = {'page_title': 'стартовая'}
    return render(request, 'mainapp/index.html', context)


def items(request):
    gived_items = ItemModel.objects.filter(is_active=True, worker__is_active=True, item_type__is_active=True)
    city_list = CityModel.objects.filter(is_active=True)
    company_list = CompanyModel.objects.filter(is_active=True)
    departament_list = DepartamentModel.objects.filter(is_active=True)
    brigadier_list = WorkerModel.objects.filter(is_brig=True, is_active=True)
    item_list = ItemTypeModel.objects.filter(is_active=True)
    context = {'page_title': 'список предметов',
               'items': gived_items,
               'cities': city_list,
               'companies': company_list,
               'departaments': departament_list,
               'brigadiers': brigadier_list,
               'item_types': item_list,
               'today': today(),
               }
    return render(request, 'mainapp/items.html', context)


def today():
    to_day = datetime.now() + timedelta(hours=5)
    return date(to_day.year, to_day.month, to_day.day)
