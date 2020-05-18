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


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    # if created:
    #     category.save()
    #     return category
    return c

def populate():
    category_list = [
        {"name": "java"},
        {"name": "js"},
        {"name": "react"},
        {"name": "unit_testing"},
    ]

    # category = models.ForeignKey(Category)
    # title = models.CharField(max_length=120)
    # url = models.URLField()
    # views = models.IntegerField(default=0)
    java_pages = [
        {
            "title": "java variables",
            "url": "",
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
            "url": "",
            "views": 2
        }
    ]
    categories = {
        "java": java_pages,
        "js": js_pages
    }
    for category_name, pages_attached in categories.items():
        new_category = add_category(category_name)
        for page in pages_attached:
            add_page(new_category, page.get("title"), page.get("url"), page.get("views"))


def print_info():
    all_cat = Category.objects.all()
    for cat in all_cat:
        print(f"{cat}->")
        pages_attached = Page.objects.filter(category=cat)
        for i, page in enumerate(pages_attached):
            print(f"page {i} -> {page}")


if __name__ == "__main__":
    print("starting reango popuating script...")
    populate()
