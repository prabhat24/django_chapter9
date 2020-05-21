import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rango_project.settings')
import django

django.setup()
from rango.models import Page, Category


def add_page(category, title, url, views=0):
    (page, created) = Page.objects.get_or_create(category=category, title=title, url=url, views=views)
    if created:
        page.save()
    return page


def add_category(name, views, likes):
    (cat_obj, created) = Category.objects.get_or_create(name=name, views=views, likes=likes)
    if created:
        print(f"category {name} created")
    return cat_obj


def populate():
    java_pages = [
        {
            "title": "java variables",
            "url": "https://www.javatpoint.com/java-variables",
            "views": 3
        }
    ]
    js_pages = [
        {
            "title": "js variables",
            "url": "",
            "views": 5
        },
        {
            "title": "js datatypes",
            "url": "https://www.javatpoint.com/javascript-variable",
            "views": 2
        }
    ]
    categories = [
        {
            "name": "java",
            "pages": java_pages,
            "views": 2,
            "likes": 0
        },
        {
            "name": "js",
            "pages": js_pages,
            "views": 20,
            "likes": 5
        }
    ]
    for cat_dict in categories:
        new_category = add_category(cat_dict.get("name"), cat_dict.get("views"), cat_dict.get("likes"))
        for page in cat_dict.get("pages"):
            add_page(new_category, page.get("title"), page.get("url"), page.get("views"))


def print_info():
    all_cat = Category.objects.all()
    for cat in all_cat:
        print(f"{cat}->")
        pages_attached = Page.objects.filter(category=cat)
        for i, page in enumerate(pages_attached):
            print(f"page {i} -> {page}")


if __name__ == "__main__":
    print("starting rango population script...")
    populate()
