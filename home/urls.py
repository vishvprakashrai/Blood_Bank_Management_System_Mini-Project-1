from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blood', views.blood, name='blood'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('news', views.news, name='news'),
    path('login/', views.login_all, name='login'),
    path('logout', views.logout_all, name='logout'),
    path('registerdonor', views.registerdonor, name='registerdonor'),
    path('registerseeker', views.registerseeker, name='registerseeker'),
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('donordashboard', views.donordashboard, name='donordashboard'),
    path('seekerdashboard', views.seekerdashboard, name='seekerdashboard'),
    path('adminaction', views.adminaction, name='adminaction'),
    path('donordetails/', views.donordetails, name='donordetails'),
    path('seekerdetails/', views.seekerdetails, name='seekerdetails'),
    path('seekerprofile/', views.seekerprofile, name='seekerprofile'),
    path('donorprofile/', views.donorprofile, name='donorprofile')
    
]
