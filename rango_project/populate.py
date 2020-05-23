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
            "views": 81
        },
        {
            "title": "java-identifiers",
            "url": "https://www.geeksforgeeks.org/java-identifiers/",
            "views": 4
        },
        {
            "title": "data types in java",
            "url": "https://www.geeksforgeeks.org/data-types-in-java/",
            "views": 2
        },
        {
            "title": "enum in java",
            "url": "https://www.geeksforgeeks.org/enum-in-java/",
            "views": 76
        },
        {
            "title": "enum-customized-value-java",
            "url": "https://www.geeksforgeeks.org/enum-customized-value-java/",
            "views": 3
        },
        {
            "title": "java variables",
            "url": "https://www.javatpoint.com/java-variables",
            "views": 65
        },
        {
            "title": "blank-final-in-java",
            "url": "https://www.geeksforgeeks.org/blank-final-in-java/",
            "views": 4
        },
        {
            "title": "java variables",
            "url": "https://www.javatpoint.com/java-variables",
            "views": 22
        },
        {
            "title": "stringbuffer",
            "url": "https://www.geeksforgeeks.org/stringbuffer-appendcodepoint-method-in-java/",
            "views": 10
        }
    ]
    js_pages = [
        {
            "title": "Awesome JS",
            "url": "https://www.geeksforgeeks.org/how-to-be-a-javascript-developer-without-knowing-javascript/",
            "views": 7
        },
        {
            "title": "js datatypes",
            "url": "https://www.javatpoint.com/javascript-variable",
            "views": 8
        },
        {
            "title": "variable-scopes-in-javascript",
            "url": "https://www.geeksforgeeks.org/understanding-variable-scopes-in-javascript/",
            "views": 7
        },
        {
            "title": "understanding-basic-javascript-codes",
            "url": "https://www.geeksforgeeks.org/understanding-basic-javascript-codes/",
            "views": 3
        },
        {
            "title": "else-statement",
            "url": "https://www.geeksforgeeks.org/else-statement-javascript/",
            "views": 15
        },
        {
            "title": "switch-case-javascript",
            "url": "https://www.geeksforgeeks.org/switch-case-javascript/",
            "views": 23
        },
        {
            "title": "loops-in-javascript",
            "url": "https://www.geeksforgeeks.org/loops-in-javascript/",
            "views": 26
        },
        {
            "title": "functions-in-javascript",
            "url": "https://www.geeksforgeeks.org/functions-in-javascript/",
            "views": 23
        },
        {
            "title": "javascript-modules",
            "url": "https://www.geeksforgeeks.org/javascript-modules/",
            "views": 25
        },
        {
            "title": "javascript-importing-and-exporting-modules",
            "url": "https://www.geeksforgeeks.org/javascript-importing-and-exporting-modules/",
            "views": 21
        },
        {
            "title": "javascript-hoisting",
            "url": "https://www.geeksforgeeks.org/javascript-hoisting/",
            "views": 2
        },
        {
            "title": "javascript-callbacks",
            "url": "https://www.geeksforgeeks.org/javascript-callbacks/",
            "views": 14
        }
    ]
    python_pages = [
        {
            "title": "python-language",
            "url": "https://www.geeksforgeeks.org/python-language-introduction/",
            "views": 17
        },
        {
            "title": "python-3-basics",
            "url": "https://www.geeksforgeeks.org/python-3-basics/",
            "views": 16
        },
        {
            "title": "python-the-new-generation-language",
            "url": "https://www.geeksforgeeks.org/python-the-new-generation-language/",
            "views": 15
        },
        {
            "title": "important-differences-between-python-2-x-and-python-3-x",
            "url": "https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/",
            "views": 14
        },
        {
            "title": "keywords-python-set-1",
            "url": "https://www.geeksforgeeks.org/keywords-python-set-1/",
            "views": 12
        },
        {
            "title": "keywords-python-set-2",
            "url": "https://www.geeksforgeeks.org/keywords-python-set-2/",
            "views": 6
        },
        {
            "title": "namespaces-and-scope",
            "url": "https://www.geeksforgeeks.org/namespaces-and-scope-in-python/",
            "views": 23
        },
        {
            "title": "statement-indentation",
            "url": "https://www.geeksforgeeks.org/statement-indentation-and-comment-in-python/",
            "views": 4
        }
    ]
    django_pages = [
        {
            "title": "django-tutorial",
            "url": "https://www.geeksforgeeks.org/django-tutorial/",
            "views": 23
        },
        {
            "title": "django-basics",
            "url": "https://www.geeksforgeeks.org/django-basics/",
            "views": 42
        },
        {
            "title": "django-introduction-and-installation",
            "url": "https://www.geeksforgeeks.org/django-introduction-and-installation/",
            "views": 3
        },
        {
            "title": "django-forms",
            "url": "https://www.geeksforgeeks.org/django-forms/",
            "views": 12
        },
        {
            "title": "views-in-django",
            "url": "https://www.geeksforgeeks.org/views-in-django-python/",
            "views": 14
        },
        {
            "title": "django-models",
            "url": "https://www.geeksforgeeks.org/django-models/",
            "views": 22
        },
        {
            "title": "python-todo-webapp-using-django",
            "url": "https://www.geeksforgeeks.org/python-todo-webapp-using-django/",
            "views": 41
        }
    ]
    categories = [
        {
            "name": "java",
            "pages": java_pages,
            "views": 30,
            "likes": 40
        },
        {
            "name": "js",
            "pages": js_pages,
            "views": 20,
            "likes": 53
        },
        {
            "name": "python",
            "pages": python_pages,
            "views": 34,
            "likes": 42
        },
        {
            "name": "Django",
            "pages": django_pages,
            "views": 23,
            "likes": 52
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
