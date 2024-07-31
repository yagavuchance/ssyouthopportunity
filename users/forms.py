from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['choice','username', 'email', 'password1', 'password2']
        labels = {
            'choice': 'Role',
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password1': ' Confirm_Password',
            
        }
        widgets = {
            'choice': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            
        }
class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        labels = {
            
            'username': 'Username',
            'password': 'Password',
            
        }
        widgets = {
           
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
        }

#password reset

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
    )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}),
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}),
    )