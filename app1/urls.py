from django.contrib import admin
from django.urls import path, include
from app1 import views


urlpatterns = [
    path('', views.password_list, name='list'),
    path('add/', views.add_userpassword, name= 'add'),
    path('details/<int:pk>/', views.details_userpassword, name= 'details'),
    path('edit/<int:pk>/', views.edit_userpassword, name= 'edit'),
    path('delete/<int:pk>/', views.delete_userpassword, name= 'delete'),
]
