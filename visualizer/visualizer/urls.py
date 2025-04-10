"""
URL configuration for visualizer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from signup.views import signup
from login.views import login
from login.views import logout
from pages.views import about, arrays, dashboard, index, linkedlist, queue, searchtypes, sorttypes, stack


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('signup/',signup),
    path('login/',login),
    path('logout/',logout),
    path('about/',about),
    path('dashboard/',dashboard),
    path('index/',index),
    path('arrays/',arrays),
    path('linkedlist/',linkedlist),
    path('stack/',stack),
    path('queue/',queue),
    path('searchtypes/',searchtypes),
    path('sorttypes/',sorttypes),
]
