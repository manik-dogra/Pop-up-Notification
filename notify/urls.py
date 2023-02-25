from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path("send_function", views.send_function),
    path('admin/', admin.site.urls),
    
]
