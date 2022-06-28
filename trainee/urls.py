from django.contrib import admin
from django.urls import include, path
from trainee import views

urlpatterns = [
    path('add/', views.create_trainee, name='trainees'),
    path('list/', views.trainees_list, name='trainees-list'),
]
