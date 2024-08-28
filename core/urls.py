from django.urls import path
from . import views

 # Import only JobSitemap


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('privacy/', views.privacy, name='privacy'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('success/', views.success, name='success'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
  
]
