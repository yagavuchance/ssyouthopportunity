from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

from django.contrib.auth import views as auth_views
from django.urls import path
from .import views


urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('registration_success/', views.registration_success, name='registration_success'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login_success/', views.login_success, name='login_success'),
    path('logout_success/', views.logout_success, name='logout_success'),

    
]
