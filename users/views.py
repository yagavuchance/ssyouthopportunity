from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm, CustomSetPasswordForm
from django.shortcuts import render, redirect
from .forms import JobseekerRegistrationForm, EmployerRegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'jobseeker':
            form = JobseekerRegistrationForm(request.POST, prefix='jobseeker')
        else:
            form = EmployerRegistrationForm(request.POST, prefix='employer')

        if form.is_valid():
            user = form.save(commit=False)
            user.choice = form_type  # Set the user's role based on the form type
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. Please log in.')
            return redirect('login')
        else:
            # If the form is invalid, maintain the current form state
            if form_type == 'jobseeker':
                jobseeker_form = form
                employer_form = EmployerRegistrationForm(prefix='employer')
            else:
                employer_form = form
                jobseeker_form = JobseekerRegistrationForm(prefix='jobseeker')
    else:
        jobseeker_form = JobseekerRegistrationForm(prefix='jobseeker')
        employer_form = EmployerRegistrationForm(prefix='employer')

    return render(request, 'users/register.html', {
        'jobseeker_form': jobseeker_form,
        'employer_form': employer_form,
    })


def registration_success(request):
    return render(request, 'users/login_success.html')



def login_user(request):
    next_url = request.GET.get('next')  # Capture the 'next' parameter from the GET request
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You have successfully logged in. welcome {username}')
                return redirect('login_success')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form, 'next': next_url})


def login_success(request):
    return render(request, 'users/login_success.html')


def logout_user(request):
    if request.method =='POST':
     logout(request)
     messages.success(request, f'logout successfully')
    return redirect('logout_success')

def logout_success(request):
    return render(request, 'users/logout_success.html')

#password view
class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_form.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'