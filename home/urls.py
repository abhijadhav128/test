from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name = 'home'),
    path('tasks/',views.tasks, name = 'tasks'),
    path('delete/<int:pk>/', views.delete_task , name="deletedata"),
    path('update/<int:pk>/', views.update_view , name="updatedata"),



]