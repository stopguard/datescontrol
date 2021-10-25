from django.contrib import admin

# Register your models here.
from workersapp.models import CityModel, CompanyModel, DepartamentModel, WorkerModel

admin.site.register(CityModel)
admin.site.register(CompanyModel)
admin.site.register(DepartamentModel)
admin.site.register(WorkerModel)
