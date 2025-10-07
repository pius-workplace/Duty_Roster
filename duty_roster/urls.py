from django.contrib import admin
from django.urls import path, include, re_path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    re_path(r'^(?!api/).*', index, name='index'),
]
