from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^$', views.index, name='index'),
    url(r'^upload$', views.upload, name='upload')
]

