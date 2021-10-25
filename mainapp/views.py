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
    worker_list = [
        {
            'city': 'г. Уфа',
            'company': {'name': 'ООО СВОС', 'status': 'VV'},
            'departament': {'name': 'Отдел подключений физических лиц', 'status': 'VV'},
            'brig_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'VV'},
            'worker_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'VV'},
        },
    ]
    city_list = ['Уфа', 'Стерлитамак', 'Нижний Новгород', ]
    company_list = ['Уфанет', 'СВОС', ]
    departament_list = ['ОПЮЛ', 'СИ', 'Монтажный отдел']
    brigadier_list = ['dsfdsfsdfds', 'fdsfdsfsdfdsf', 'ffgggddssss']
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
    docs = [
        {
            'group': 'Электробезопасность',
            'name': 'Электробезопасность 2гр',
            'change_interval': 12,
            'test_interval': 12,
        },
        {
            'group': 'Электробезопасность',
            'name': 'Электробезопасность 3гр',
            'change_interval': 12,
            'test_interval': 12,
        },
        {
            'group': 'Электробезопасность',
            'name': 'Электробезопасность 4гр',
            'change_interval': 12,
            'test_interval': 12,
        },
        {
            'group': 'Электробезопасность',
            'name': 'Электробезопасность 5гр',
            'change_interval': 12,
            'test_interval': 12,
        },
        {
            'group': 'Высота',
            'name': 'Высота 1гр',
            'change_interval': 36,
            'test_interval': 12,
        },
        {
            'group': 'Высота',
            'name': 'Высота 2гр',
            'change_interval': 36,
            'test_interval': 12,
        },
        {
            'group': 'Высота',
            'name': 'Высота 3гр',
            'change_interval': 60,
            'test_interval': 12,
        },
    ]
    tools = [
        {
            'group': 'Лестницы',
            'name': 'Лестница 3*6',
            'test_interval': 12,
        },
        {
            'group': 'Лестницы',
            'name': 'Лестница 3*9',
            'test_interval': 12,
        },
        {
            'group': 'Лестницы',
            'name': 'Лестница 3*11',
            'test_interval': 12,
        },
        {
            'group': 'Лестницы',
            'name': 'Лестница 3*12',
            'test_interval': 12,
        },
        {
            'group': 'Электроинструмент',
            'name': 'Перфоратор аккум.',
            'test_interval': 6,
        },
        {
            'group': 'Электроинструмент',
            'name': 'Перфоратор пров.',
            'test_interval': 6,
        },
        {
            'group': 'Электроинструмент',
            'name': 'Перфоратор больш.',
            'test_interval': 6,
        },
        {
            'group': 'Электроинструмент',
            'name': 'Шуруповёрт',
            'test_interval': 6,
        },
        {
            'group': 'Электроинструмент',
            'name': 'Болгарка аккум.',
            'test_interval': 6,
        },
    ]
    context = {'page_title': 'типы предметов',
               'docs': docs,
               'tools': tools,
               'today': today,
               }
    return render(request, 'mainapp/item_types.html', context)
