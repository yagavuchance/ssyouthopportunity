from django.urls import path
from .import views

urlpatterns = [
    path('',views.fellowship,name='fellowship')
]
