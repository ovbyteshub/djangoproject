from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('tasks/create', views.create_task),
    path('projects/create', views.create_project),
    ]