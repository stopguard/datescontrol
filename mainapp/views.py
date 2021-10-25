from django.shortcuts import render
from datetime import date, timedelta, datetime
from mainapp.models import ItemModel, WorkerModel, ItemTypeModel, \
    CityModel, CompanyModel, DepartamentModel, ItemGroupModel


# Create your views here.
def index(request):
    context = {'page_title': 'стартовая'}
    return render(request, 'mainapp/index.html', context)


def items(request):
    today = datetime.now() + timedelta(hours=5)
    today = date(today.year, today.month, today.day)
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
               'today': today,
               }
    return render(request, 'mainapp/items.html', context)


def departaments(request):
    today = datetime.now() + timedelta(hours=5)
    today = date(today.year, today.month, today.day)
    worker_list = WorkerModel.objects.filter(is_active=True)
    city_list = CityModel.objects.filter(is_active=True)
    company_list = CompanyModel.objects.filter(is_active=True)
    departament_list = DepartamentModel.objects.filter(is_active=True)
    brigadier_list = WorkerModel.objects.filter(is_brig=True, is_active=True)
    context = {'page_title': 'список сотрудников',
               'cities': city_list,
               'companies': company_list,
               'departaments': departament_list,
               'brigadiers': brigadier_list,
               'workers': worker_list,
               'today': today,
               }
    return render(request, 'mainapp/departaments.html', context)


def item_types(request):
    today = datetime.now() + timedelta(hours=5)
    today = date(today.year, today.month, today.day)
    docs = ItemTypeModel.objects.filter(is_active=True, group__doc_or_tool='Удостоверение')
    tools = ItemTypeModel.objects.filter(is_active=True, group__doc_or_tool='Инструмент')
    context = {'page_title': 'типы предметов',
               'docs': docs,
               'tools': tools,
               'today': today,
               }
    return render(request, 'mainapp/item_types.html', context)
