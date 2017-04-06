from django.conf.urls import url
from . import views
from . import search

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^startup/$', views.startups, name='startup'),
    url(r'^startup/(?P<startup_name>[^/]+)/$', views.startup_detail, name='startup_page'),
    url(r'^news/$', views.news, name='news'),
    url(r'^internship/$', views.internships, name='internship'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^search/$', views.search, name='search'),
    url(r'^city/(?P<city_name>[^/]+)$', views.city, name='city')
]
