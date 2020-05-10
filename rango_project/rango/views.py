from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    context = {
        "boldmessage": "I am Rango"
    }
    return render(request, 'rango/home.html', context)


def about_us(request):
    context = {
        "name": "prabhat"
    }
    return render(request, 'rango/about.html', context)
