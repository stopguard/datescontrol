from django.urls import path

import workersapp.views as workersapp

app_name = 'workersapp'

urlpatterns = [
    path('', workersapp.workers, name='index'),
    path('city_filter/<int:city_pk>/', workersapp.city_filter, name='city_filter'),
    path('company_filter/<int:company_pk>/', workersapp.company_filter, name='company_filter'),
    path('departament_filter/<int:departament_pk>/', workersapp.departament_filter, name='departament_filter'),
    path('brig_filter/<int:brig_pk>/', workersapp.brig_filter, name='brig_filter'),
    path('info/<int:pk>/', workersapp.info, name='info'),
]
