from django.shortcuts import render
from datetime import date, timedelta, datetime


# Create your views here.
def index(request):
    context = {'page_title': 'стартовая'}
    return render(request, 'mainapp/index.html', context)


def items(request):
    today = datetime.now() + timedelta(hours=5)
    today = date(today.year, today.month, today.day)
    gived_items = [
        {
            'company': 'ООО СВОС',
            'departament': 'Отдел подключений физических лиц',
            'worker_name': 'Удинский Дмитрий Игоревич',
            'item_class': 'doc',
            'item_name': 'Электробезопасность 3гр',
            'inv_num': 'КА1234',
            'check_for': date(2018, 10, 2),
            'test_for': date(2020, 11, 20),
            'check_to': date(2022, 10, 2),
            'test_to': date(2022, 11, 20),
        },
        {
            'company': 'ООО СВОС',
            'departament': 'Отдел подключений физических лиц',
            'worker_name': 'Удинский Дмитрий Игоревич',
            'item_class': 'tool',
            'item_name': 'Лестница 3*9',
            'inv_num': 'КА1234',
            'check_for': date(2018, 10, 2),
            'check_to': date(2021, 10, 2),
        },
        {
            'company': 'ООО СВОС',
            'departament': 'Отдел подключений физических лиц',
            'worker_name': 'Удинский Дмитрий Игоревич',
            'item_class': 'doc',
            'item_name': 'ПТМ',
            'inv_num': 'КА1234',
            'check_for': date(2020, 11, 10),
            'test_for': date(2020, 11, 10),
            'check_to': date(2021, 11, 10),
            'test_to': date(2021, 11, 10),
        },
        {
            'company': 'ООО СВОС',
            'departament': 'Отдел подключений физических лиц',
            'worker_name': 'Удинский Дмитрий Игоревич',
            'item_class': 'tool',
            'item_name': 'Лестница динамика',
            'inv_num': 'КА1234',
            'check_for': date(2018, 10, 2),
            'check_to': date(2021, 10, 2),
        },
        {
            'company': 'ООО СВОС',
            'departament': 'Отдел подключений физических лиц',
            'worker_name': 'Удинский Дмитрий Игоревич',
            'item_class': 'tool',
            'item_name': 'Лестница 3*6',
            'inv_num': 'КА1234',
            'check_for': date(2018, 12, 2),
            'check_to': date(2021, 12, 2),
        },
    ]
    city_list = ['Уфа', 'Стерлитамак', 'Нижний Новгород', ]
    company_list = ['Уфанет', 'СВОС', ]
    departament_list = ['ОПЮЛ', 'СИ', 'Монтажный отдел']
    brigadier_list = ['dsfdsfsdfds', 'fdsfdsfsdfdsf', 'ffgggddssss']
    item_list = ['Электробезопасность 5гр', 'ПТМ', 'Высота 2гр']
    for el in gived_items:
        if el['item_class'] == 'doc' and el['check_to'] > el['test_to']:
            el['check_to'] = el['test_to']
        delta = (el['check_to'] - today).days
        if delta > 90:
            el['status'] = 'OK'
        elif delta > 30:
            el['status'] = 'OO'
        elif delta > 0:
            el['status'] = 'VV'
        else:
            el['status'] = 'XX'
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
        {
            'city': 'г. Уфа',
            'company': {'name': 'ООО СВОС', 'status': 'XX'},
            'departament': {'name': 'Отдел подключений физических лиц', 'status': 'XX'},
            'brig_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'XX'},
            'worker_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'XX'},
        },
        {
            'city': 'г. Уфа',
            'company': {'name': 'ООО СВОС', 'status': 'OK'},
            'departament': {'name': 'Отдел подключений физических лиц', 'status': 'OK'},
            'brig_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OK'},
            'worker_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OK'},
        },
        {
            'city': 'г. Уфа',
            'company': {'name': 'ООО СВОС', 'status': 'OO'},
            'departament': {'name': 'Отдел подключений физических лиц', 'status': 'OO'},
            'brig_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OO'},
            'worker_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OO'},
        },
        {
            'city': 'г. Уфа',
            'company': {'name': 'ООО СВОС', 'status': 'OK'},
            'departament': {'name': 'Отдел подключений физических лиц', 'status': 'OK'},
            'brig_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OK'},
            'worker_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OK'},
        },
        {
            'city': 'г. Уфа',
            'company': {'name': 'ООО СВОС', 'status': 'OK'},
            'departament': {'name': 'Отдел подключений физических лиц', 'status': 'OK'},
            'brig_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OK'},
            'worker_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OK'},
        },
        {
            'city': 'г. Уфа',
            'company': {'name': 'ООО СВОС', 'status': 'OK'},
            'departament': {'name': 'Отдел подключений физических лиц', 'status': 'OK'},
            'brig_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OK'},
            'worker_name': {'name': 'Удинский Дмитрий Игоревич', 'status': 'OK'},
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
    context = {'page_title': 'типы предметов'}
    return render(request, 'mainapp/item_types.html', context)
