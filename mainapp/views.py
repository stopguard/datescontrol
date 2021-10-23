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
            'test_for': date(2018, 10, 2),
            'change_for': date(2020, 11, 20),
            'test_to': date(2022, 10, 2),
            'change_to': date(2022, 11, 20),
        },
        {
            'company': 'ООО СВОС',
            'departament': 'Отдел подключений физических лиц',
            'worker_name': 'Удинский Дмитрий Игоревич',
            'item_class': 'tool',
            'item_name': 'Лестница 3*9',
            'inv_num': 'КА1234',
            'test_for': date(2018, 10, 2),
            'test_to': date(2021, 10, 2),
        },
        {
            'company': 'ООО СВОС',
            'departament': 'Отдел подключений физических лиц',
            'worker_name': 'Удинский Дмитрий Игоревич',
            'item_class': 'doc',
            'item_name': 'ПТМ',
            'inv_num': 'КА1234',
            'test_for': date(2020, 11, 10),
            'change_for': date(2020, 11, 10),
            'test_to': date(2021, 11, 10),
            'change_to': date(2021, 11, 10),
        },
        {
            'company': 'ООО СВОС',
            'departament': 'Отдел подключений физических лиц',
            'worker_name': 'Удинский Дмитрий Игоревич',
            'item_class': 'tool',
            'item_name': 'Лестница динамика',
            'inv_num': 'КА1234',
            'test_for': date(2018, 10, 2),
            'test_to': date(2021, 10, 2),
        },
        {
            'company': 'ООО СВОС',
            'departament': 'Отдел подключений физических лиц',
            'worker_name': 'Удинский Дмитрий Игоревич',
            'item_class': 'tool',
            'item_name': 'Лестница 3*6',
            'inv_num': 'КА1234',
            'test_for': date(2018, 12, 2),
            'test_to': date(2021, 12, 2),
        },
    ]
    city_list = ['Уфа', 'Стерлитамак', 'Нижний Новгород', ]
    company_list = ['Уфанет', 'СВОС', ]
    departament_list = ['ОПЮЛ', 'СИ', 'Монтажный отдел']
    brigadier_list = ['dsfdsfsdfds', 'fdsfdsfsdfdsf', 'ffgggddssss']
    item_list = ['Электробезопасность 5гр', 'ПТМ', 'Высота 2гр']
    for el in gived_items:
        if el['item_class'] == 'doc' and el['test_to'] > el['change_to']:
            el['test_to'] = el['change_to']
        delta = (el['test_to'] - today).days
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
