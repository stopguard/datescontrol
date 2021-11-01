from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('items/', mainapp.items, name='items'),
    path('items/city_filter/<int:city_pk>/', mainapp.city_filter, name='city_filter'),
    path('items/company_filter/<int:company_pk>/', mainapp.company_filter, name='company_filter'),
    path('items/departament_filter/<int:departament_pk>/', mainapp.departament_filter, name='departament_filter'),
    path('items/brig_filter/<int:brig_pk>/', mainapp.brig_filter, name='brig_filter'),
    path('items/worker_filter/<int:worker_pk>', mainapp.worker_filter, name='worker_filter'),
    path('items/group_filter/<int:item_group_pk>', mainapp.group_filter, name='group_filter'),
    path('items/type_filter/<int:item_type_pk>', mainapp.type_filter, name='type_filter'),
]
