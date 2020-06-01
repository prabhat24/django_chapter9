from django.http import HttpResponse
from django.shortcuts import render
from .models import Page, Category
from .forms import CategoryForm, PageForm


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
        "pages": five_pages,
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
        "category_name_slug" : category_name_slug,
        "pages": related_pages
    }
    return render(request, "rango/category.html", context)


def about_us(request):
    context = {
        "name": "prabhat"
    }
    return render(request, 'rango/about.html', context)


def add_category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home_view(request)
        else:
            # form may contain errors
            print(f"errors : {form.errors}")
    context = {
        'form': form
    }
    return render(request, "rango/add_category.html", context)


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = PageForm()
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.save()
            return view_category(request,category_name_slug)
        else:
            print(f"errors {form.errors}")
    context = {
        "form": form,
        "category" : category,
        "category_name_slug" : category_name_slug
    }
    return render(request, f"rango/add_page.html", context)
