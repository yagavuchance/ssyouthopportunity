from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import JobSitemap  # Import only JobSitemap

sitemaps = {
    'jobs': JobSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('privacy/', views.privacy, name='privacy'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('success/', views.success, name='success'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
