from django.contrib import admin

from mainapp.models import CityModel, CompanyModel, DepartamentModel, \
    WorkerModel, ItemGroupModel, ItemTypeModel, ItemModel

admin.site.register(CityModel)
admin.site.register(CompanyModel)
admin.site.register(DepartamentModel)
admin.site.register(WorkerModel)
admin.site.register(ItemGroupModel)
admin.site.register(ItemTypeModel)
admin.site.register(ItemModel)
