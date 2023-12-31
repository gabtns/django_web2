from django.contrib import admin
from django.urls import path,include
from . import views 
from django.conf import settings

urlpatterns = [
    path('service/', views.serv, name="service"),
]

if settings.DEBUG: 
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)