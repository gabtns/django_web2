from django.contrib import admin
from django.urls import path,include
from . import views 


urlpatterns = [
    path("", views.home, name="home"),
    path('visite/',views.visita, name="visite"),
    path('blog/', views.blogs, name="blog"),
    path('history/', views.historia, name="history"),
    path('other/',views.otros, name="other"),
    path('contacto/',views.contacto, name="contacto"),
]

