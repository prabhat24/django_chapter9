from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse(f"this is rango application homepage. <br>"
                        f"<a href='/rango/about/'>About</a>.")

def about_us(request):
    return HttpResponse(f"Rango says here is the about page.<br>"
                        f"<a href='/rango/home/'>Home</a>")