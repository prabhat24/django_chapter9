from django.conf.urls import url
from . import views

app_name = 'rango'
urlpatterns = [
    url(r'^$', views.home_view, name="home"),
    url(r'^about', views.about_us, name="about"),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.view_category, name='view_category'),
    url(r'^add_category/$', views.add_category, name="add_category"),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name="add_page"),
    url(r'^register/$', views.register_user, name="register"),
    url(r'^login/$', views.user_login, name="login"),
    url(r'^logout/$', views.user_logout, name='logout'),
]
