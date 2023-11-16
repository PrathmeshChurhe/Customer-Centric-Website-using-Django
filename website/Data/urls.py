from django.contrib import admin
from django.urls import path
from Data import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about, name='about'),
    path('services', views.services, name='services'),
    path('technology', views.technology, name='technology'),
    path('team', views.team, name='team'),
    path('clients', views.clients, name='clients'),
    path('contact', views.contact, name='contact')
    # path('login', views.login, name='login')
]
