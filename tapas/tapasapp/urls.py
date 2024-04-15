from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('basic_list', views.basic_list, name='basic_list'),
    path('manage_account/<int:pk>/', views.manage_account, name='manage_account'),
    path('change_password/<int:pk>/', views.change_password, name='change_password'),
]