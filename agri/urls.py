from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage , name='home'),
    path('credit/', views.credit , name='credit'),
    path('privacy/', views.privacy , name='privacy&policy'),
    path('about/', views.about , name='about'),
    path('terms/', views.terms , name='terms&cond'),
    path('soilMore/', views.soil_more , name='soil_more'),
    path('fertMore/', views.fert_more , name='fert_more'),
    path('plantMore/', views.plant_more , name='plant_more'),
    path('rainMore/', views.rain_more , name='rain_more'),
    path('manageMore/', views.manage_more , name='manage_more'),
]
