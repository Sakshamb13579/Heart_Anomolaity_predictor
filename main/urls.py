from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.aboutus, name='about'),
    path('contact/', views.contactus, name='contact'),
]