from django.contrib import admin

# Register your models here.
from itemtypesapp.models import ItemGroupModel, ItemTypeModel

admin.site.register(ItemGroupModel)
admin.site.register(ItemTypeModel)
