from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('', include('mainapp.urls', namespace='main')),
    path('itemtypes/', include('itemtypesapp.urls', namespace='itemtypes')),
    path('workers/', include('workersapp.urls', namespace='workers')),
    path('auth/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
