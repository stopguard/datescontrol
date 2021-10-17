from django.shortcuts import render
from datetime import date, timedelta, datetime


# Create your views here.
def index(request):
    context = {'page_title': 'стартовая'}
    return render(request, 'mainapp/index.html', context)


def items(request):
    today = datetime.now() + timedelta(hours=5)
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
            'check_to': date(2021, 10, 2),
            'test_to': date(2021, 11, 20),
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
    for el in gived_items:
        if el['item_class'] == 'doc' and el['check_to'] > el['test_to']:
            el['check_to'] = el['test_to']
    city_list = [
        ''
    ]
    context = {'page_title': 'список предметов',
               'items': gived_items,
               'today': today}
    return render(request, 'mainapp/items.html', context)


def departaments(request):
    context = {'page_title': 'список сотрудников'}
    return render(request, 'mainapp/departaments.html', context)


def item_types(request):
    context = {'page_title': 'типы предметов'}
    return render(request, 'mainapp/item_types.html', context)
