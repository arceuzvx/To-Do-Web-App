from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:pk>/', views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('toggle-complete/<int:pk>/', views.todo_toggle_complete, name='todo_toggle_complete'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
] 