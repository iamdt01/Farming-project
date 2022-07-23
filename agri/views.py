from django.shortcuts import render , redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib import messages


def homepage(request):
    return render(request, 'home.html')


def credit(request):
    return render(request, 'profile.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')


def about(request):
    return render(request, 'about.html')


def soil_more(request):
    return render(request, 'soil_more.html')


def fert_more(request):
    return render(request, 'fert_more.html')


def rain_more(request):
    return render(request, 'rain_more.html')


def plant_more(request):
    return render(request, 'plant_more.html')


def manage_more(request):
    return render(request, 'manage_more.html')