from.models import mychart
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('chart',views.chart,name='chart'),
    path('singup',views.singup,name='singup')


]
