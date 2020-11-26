from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('webhooks/', views.MessageCreateViewSet.as_view()),
    path('events/', views.EventListViewSet.as_view()),
]