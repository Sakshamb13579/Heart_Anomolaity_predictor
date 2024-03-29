from django.urls import path
from .models import *
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('form/', views.additional_form, name='additional_form'),
]