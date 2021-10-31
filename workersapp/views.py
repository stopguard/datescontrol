from datetime import date, timedelta, datetime

from django.shortcuts import render

from workersapp.models import CityModel, CompanyModel, DepartamentModel, WorkerModel


# Create your views here.
def workers(request):
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
               'today': today(),
               }
    return render(request, 'workersapp/workers.html', context)


def today():
    to_day = datetime.now() + timedelta(hours=5)
    return date(to_day.year, to_day.month, to_day.day)
