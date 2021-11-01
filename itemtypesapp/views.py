from datetime import date, timedelta, datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from itemtypesapp.models import ItemTypeModel


@login_required
def item_types(request):
    if not (request.user.is_linked or request.user.is_superuser):
        messages.warning(request, 'Ваша учётная запись не привязана к работнику! '
                                  'Обратитесь к вашему руководителю или администратору.')
        return HttpResponseRedirect(reverse('main:index'))
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
