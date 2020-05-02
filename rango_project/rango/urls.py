from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.home_view, name="home"),
    url(r'^about', views.about_us, name="about_us")
]
