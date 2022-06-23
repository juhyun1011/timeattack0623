from django.contrib import admin
from django.urls import path, include
from item import views

urlpatterns = [
    path('', views.itemView.as_view()),
]
