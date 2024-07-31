from django.shortcuts import render,redirect
from jobs.models import Jobs
from scholarship.models import Scholarship
from fellowships.models import Fellowship

# Create your views here.

def index(request):
    jobs_list = Jobs.objects.filter(status ='active')
    scholarship_list = Scholarship.objects.all()[:4]
    fellowship_list = Fellowship.objects.all()[:5]
    context= {
        'jobs_list': jobs_list,
        'scholarship_list': scholarship_list,
        'fellowship_list': fellowship_list
    }
    return render(request,'cores/index.html',context)

def about(request):
    return render(request,'cores/about.html')


def search(request):
    query = request.GET.get('q')
    jobs_list = []
    scholarship_list=[]
    fellowship_list=[]

    if query:
        jobs_list = Jobs.objects.filter(title__icontains=query)
        scholarship_list = Scholarship.objects.filter(title__icontains=query)
        fellowship_list = Fellowship.objects.filter(title__icontains=query)

    context = {
        'query': query,
        'jobs_list': jobs_list,
        'scholarship_list': scholarship_list,
        'fellowship_list': fellowship_list
    }
    return render(request, 'cores/index.html', context)

def privacy(request):
    return render(request, 'cores/privacy_policy.html')

def disclaimer(request):
    return render(request, 'cores/disclaimer.html')