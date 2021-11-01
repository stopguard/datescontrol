from datetime import date, timedelta, datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from workersapp.models import CityModel, CompanyModel, DepartamentModel, WorkerModel
from mainapp.views import is_linked, today


@login_required
def workers(request):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    worker_list = WorkerModel.objects.filter(is_active=True, is_brig=True) \
        .order_by('departament__company__city__name', 'departament__company__name', 'departament__name', 'name')
    return get_workers_response(request, worker_list)


@login_required
def city_filter(request, city_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    detail = 'City'
    worker_list = get_object_or_404(CityModel, pk=city_pk).workers(brig_only=True) \
        .order_by('departament__company__name', 'departament__name', 'name')
    return get_workers_response(request, worker_list, detail)


@login_required
def company_filter(request, company_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    detail = 'Company'
    worker_list = get_object_or_404(CompanyModel, pk=company_pk).workers(brig_only=True) \
        .order_by('departament__name', 'name')
    return get_workers_response(request, worker_list, detail)


@login_required
def departament_filter(request, departament_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    detail = 'Departament'
    worker_list = get_object_or_404(DepartamentModel, pk=departament_pk).workers() \
        .order_by('brig__name', 'name')
    return get_workers_response(request, worker_list, detail)


@login_required
def brig_filter(request, brig_pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    detail = 'Brig'
    worker_list = WorkerModel.objects.filter(brig_id=brig_pk).order_by('name')
    return get_workers_response(request, worker_list, detail)


@login_required
def info(request, pk):
    linked_check = is_linked(request)
    if linked_check:
        return linked_check
    worker = get_object_or_404(WorkerModel, pk=pk)
    context = {'page_title': 'Подробности о сотруднике',
               'worker': worker,
               'today': today(),
               'rules': rules(request.user, worker)
               }
    return render(request, 'workersapp/worker_info.html', context)


def get_lists(city_pk, company_pk, departament_pk):
    brigadier_list = WorkerModel.objects.filter(is_brig=True,
                                                is_active=True,
                                                departament_id=departament_pk) if departament_pk else None
    departament_list = DepartamentModel.objects.filter(is_active=True, company_id=company_pk) if company_pk else None
    company_list = CompanyModel.objects.filter(is_active=True, city_id=city_pk) if city_pk else None
    city_list = CityModel.objects.filter(is_active=True)
    return {
        'brigadier_list': brigadier_list,
        'departament_list': departament_list,
        'company_list': company_list,
        'city_list': city_list,
    }


def get_workers_response(request, worker_list, detail='All'):
    cities = CityModel.objects.filter(is_active=True)
    context = {'page_title': 'список сотрудников',
               'workers': worker_list,
               'detail': detail,
               'cities': cities,
               'today': today(),
               }
    return render(request, 'workersapp/workers.html', context)


def rules(user, worker):
    u_worker = user.linked_worker
    if u_worker:
        return departaments_rules(u_worker, worker) or departaments_rules(u_worker, worker)


def departaments_rules(checked_worker, worker):
    if checked_worker.is_departament_leader:
        return checked_worker.departament == worker.departament


def company_rules(checked_worker, worker):
    if checked_worker.is_departament_leader:
        return checked_worker.departament == worker.departament
