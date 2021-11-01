from datetime import date, timedelta, datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from mainapp.models import ItemModel
from itemtypesapp.models import ItemTypeModel
from workersapp.models import WorkerModel, CityModel, CompanyModel, DepartamentModel


def index(request):
    context = {'page_title': 'стартовая'}
    return render(request, 'mainapp/index.html', context)


@login_required
def items(request):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    return get_items_response(request)


@login_required
def group_filter(request, item_group_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    items_list = ItemModel.objects.filter(item_type__group_id=item_group_pk)
    return get_items_response(request, gived_items=items_list)


@login_required
def type_filter(request, item_type_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    items_list = ItemModel.objects.filter(item_type_id=item_type_pk)
    return get_items_response(request, gived_items=items_list)


@login_required
def city_filter(request, city_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    detail = 'City'
    workers = get_object_or_404(CityModel, pk=city_pk).workers()
    return get_items_response(request, workers, detail)


@login_required
def company_filter(request, company_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    detail = 'Company'
    workers = get_object_or_404(CompanyModel, pk=company_pk).workers()
    return get_items_response(request, workers, detail)


@login_required
def departament_filter(request, departament_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    detail = 'Departament'
    workers = get_object_or_404(DepartamentModel, pk=departament_pk).workers()
    return get_items_response(request, workers, detail)


@login_required
def brig_filter(request, brig_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    detail = 'Brig'
    workers = WorkerModel.objects.filter(is_active=True, brig_id=brig_pk)
    return get_items_response(request, workers, detail)


@login_required
def worker_filter(request, worker_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    detail = 'Worker'
    workers = WorkerModel.objects.filter(is_active=True, pk=worker_pk)
    return get_items_response(request, workers, detail)


def today():
    to_day = datetime.now() + timedelta(hours=5)
    return date(to_day.year, to_day.month, to_day.day)


def is_linked(request):
    if not (request.user.is_linked or request.user.is_superuser):
        messages.warning(request, 'Ваша учётная запись не привязана к работнику! '
                                  'Обратитесь к вашему руководителю или администратору.')
        return HttpResponseRedirect(reverse('main:index'))


def get_items_response(request, workers=None, detail='All', gived_items=None):
    workers = workers if workers else WorkerModel.objects.filter(is_active=True)
    gived_items = gived_items if gived_items else ItemModel.objects.filter(is_active=True,
                                                                           item_type__is_active=True,
                                                                           worker_id__in=workers)
    item_list = ItemTypeModel.objects.filter(is_active=True, group__is_active=True)
    cities = CityModel.objects.filter(is_active=True)
    context = {'page_title': 'список предметов',
               'detail': detail,
               'items': gived_items,
               'item_types': item_list,
               'cities': cities,
               'today': today(),
               }
    return render(request, 'mainapp/items.html', context)


def get_tools():
    pass


def get_docs():
    pass
