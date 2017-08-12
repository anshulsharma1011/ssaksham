from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

app_name = 'schedule'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^view_schedule/$',views.ViewSchedule.as_view(),name = 'view_schedule')
]
