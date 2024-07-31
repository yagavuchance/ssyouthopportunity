from django.urls import path
from .import views

urlpatterns = [
    path('E-dashboard', views.dashboard, name='E-dashboard')
]
