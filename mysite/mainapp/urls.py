from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('about', views.about, name='about'),
    url('host', views.host, name='host'),
]