from django.urls import path
from .import views

urlpatterns = [
    path('post-jobs',  views.Jobpost, name='post-jobs'),
    path('post-scholarship',  views.scholarshippost, name='post-scholarship'),
    path('edit/<int:id>/',  views.edit, name='edit'),
    path('delete-job/<int:id>/',  views.delete, name='delete-job'),
    path('job-status/<int:id>/',  views.status, name='job-status'),
    path('view-post/<int:id>/',  views.view_post, name='view-post'),
    path('posts_success/', views.post_success, name='posts_success'),
    path('edit_success/', views.edit_success, name='edit_success'),
]
