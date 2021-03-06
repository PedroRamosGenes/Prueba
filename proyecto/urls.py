"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from django.urls import path
"""
from django.contrib import admin
from django.http import HttpResponse
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.models import User
from django.shortcuts import render
from gestionUser.views import gestionUserView, confUserView, gestionPermsView, addPermsView, removePermsView, removeView, addView, verUserView, unableUserView
from proyecto.models import Proyecto
"""
from .views import proyectoView


urlpatterns = [
    path('proyecto/proyectoList/<int:proyectid>/', proyectoView, name = "proyectoView"),
]
