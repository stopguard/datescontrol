from datetime import date, timedelta, datetime

from django.shortcuts import render

from itemtypesapp.models import ItemTypeModel


# Create your views here.
def item_types(request):
    docs = ItemTypeModel.objects.filter(is_active=True, group__doc_or_tool='Удостоверение')
    tools = ItemTypeModel.objects.filter(is_active=True, group__doc_or_tool='Инструмент')
    context = {'page_title': 'типы предметов',
               'docs': docs,
               'tools': tools,
               'today': today(),
               }
    return render(request, 'itemtypesapp/item_types.html', context)


def today():
    to_day = datetime.now() + timedelta(hours=5)
    return date(to_day.year, to_day.month, to_day.day)
