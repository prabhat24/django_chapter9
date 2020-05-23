from django.http import HttpResponse
from django.shortcuts import render
from .models import Page, Category


def home_view(request):
    """
    show only first five categories
    :param request:
    :return:
    """
    five_cat = Category.objects.order_by("-views")[:5]
    five_pages = Page.objects.order_by("-views")[:5]
    context = {
        "categories": five_cat,
        "pages" : five_pages,
        "boldmessage": "Prabhat"
    }
    return render(request, 'rango/home.html', context)


def view_category(request, category_name_slug):
    try:
        category = Category.objects.filter(slug=category_name_slug)
        related_pages = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        category = None
        related_pages = None

    context = {
        "category": category,
        "pages": related_pages
    }
    return render(request, "rango/category.html", context)


def about_us(request):
    context = {
        "name": "prabhat"
    }
    return render(request, 'rango/about.html', context)
