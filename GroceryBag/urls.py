from django.contrib import admin
from django.urls import path,include
from django.urls import path

urlpatterns = [
    path('',include('webapp.urls')),
    path('admin/', admin.site.urls),
]