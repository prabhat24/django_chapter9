from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Page, Category
from .forms import CategoryForm, PageForm, UserProfileForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime


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
    }
    context.update(updated_visits_cookie_handler(request))
    response = render(request, 'rango/home.html', context)
    return response


def view_category(request, category_name_slug):
    try:
        category = Category.objects.filter(slug=category_name_slug)
        related_pages = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        category = None
        related_pages = None

    context = {
        "category": category,
        "category_name_slug": category_name_slug,
        "pages": related_pages
    }
    return render(request, "rango/category.html", context)


def about_us(request):
    context = {
        "name": "prabhat"
    }
    return render(request, 'rango/about.html', context)


@login_required
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


@login_required
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
            return view_category(request, category_name_slug)
        else:
            print(f"errors {form.errors}")
    context = {
        "form": form,
        "category": category,
        "category_name_slug": category_name_slug
    }
    return render(request, f"rango/add_page.html", context)


def register_user(request):
    registered = False

    if request.method == "POST":
        # get user data
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            user_profile = user_profile_form.save(commit=False)
            # populate user field
            user_profile.user = user
            # populate user's profile_image
            if 'profile_image' in request.FILES:
                user_profile.profile_image = request.FILES['profile_image']
            user_profile.save()
            registered = True
        else:
            # if the either of the forms are not valid
            print(f"errors: {user_form.errors}, {user_profile_form.errors}")
    else:
        # if the method is get
        user_form = UserForm()
        user_profile_form = UserProfileForm()

    context = {
        "user_form": user_form,
        "user_profile_form": user_profile_form,
        "registered": registered
    }
    return render(request, "rango/register.html", context)


def user_login(request):
    error_msg = ""
    if request.method == "POST":
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('rango:home'))
            else:
                error_msg = f" username {username} is invalid contact administrator"
                print(error_msg)
        else:
            error_msg = f" invalid username {username} and password"
            print(error_msg)
    context = {
        "error_msg": error_msg
    }
    return render(request, "rango/login.html", context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('rango:home'))


def visits_cookie_handler(request, response):
    visits = request.COOKIES.get('visits', None)
    last_visit_date = request.COOKIES.get('last_visit_date', None)
    if visits is None or last_visit_date is None:
        response.set_cookie('visits', 1)
        response.set_cookie('last_visit_date', datetime.strftime(datetime.now(), '%d%m%Y, %H:%M:%S'))
        return

    date_last_visit_date = datetime.strptime(last_visit_date, '%d%m%Y, %H:%M:%S')
    if (datetime.now() - date_last_visit_date).seconds > 10:
        visits = int(visits) + 1
        last_visit_date = datetime.strftime(datetime.now(), '%d%m%Y, %H:%M:%S')
        response.set_cookie('visits', visits)
        response.set_cookie('last_visit_date', last_visit_date)


def get_server_side_cookie(request, key, default_val):
    val = request.session.get(key)
    if not val:
        val = default_val
    return val


def updated_visits_cookie_handler(request):
    visits = get_server_side_cookie(request, 'visits', None)
    last_visit_date = get_server_side_cookie(request, 'last_visit_date', None)

    if visits is None or last_visit_date is None:
        visits = 1
        last_visit_date = datetime.strftime(datetime.now(), '%d/%m/%Y, %H:%M:%S')
        request.session['visits'] = visits
        request.session['last_visit_date'] = last_visit_date

    date_last_visit_date = datetime.strptime(last_visit_date, '%d/%m/%Y, %H:%M:%S')
    if (datetime.now() - date_last_visit_date).seconds > 10:
        visits = int(visits) + 1
        last_visit_date = datetime.strftime(datetime.now(), '%d/%m/%Y, %H:%M:%S')
        request.session['visits'] = visits
        request.session['last_visit_date'] = last_visit_date
    return {
        "visits": visits,
        "last_visit_date": last_visit_date
    }
