"""Tour_guide_provider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import demo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sign_up/', demo.views.sign_up, name='sign_up'),
    path('login/', demo.views.login, name='login'),
    path('', demo.views.homePage, name='home'),
    path('tourist/', demo.views.tourist, name='tourist'),
    path('tourist_guide/', demo.views.tourist_guide, name='tourist_guide'), #not used
    path('emergency/', demo.views.emergency, name='emergency'),
    path('tour_guide/', demo.views.tour_guide, name='tour_guide'),
    path('payment/', demo.views.payment, name='payment'),
    # path('contact', demo.views.contact),
]
