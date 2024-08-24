from django.urls import path
from . import views

urlpatterns = [
    path('',views.jobs, name='jobs'),
    path('description/<int:id>/',views.description, name='description'),
    path('downloads/<int:id>/',views.download, name='downloads'),
    


]
