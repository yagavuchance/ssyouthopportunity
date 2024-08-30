from django.shortcuts import render
from jobs.models import Jobs
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def dashboard(request):
    jobs_list = Jobs.objects.filter(created_by=request.user).order_by('-created_at')
    context={
        'jobs_list': jobs_list
    }
    return render(request, 'employ/E-dashboard.html', context)