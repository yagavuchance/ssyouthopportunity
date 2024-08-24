from django.shortcuts import render
from .models import Jobs
from django.views.generic import DetailView
from django.http import FileResponse, Http404
import os
# Create your views here.

def jobs(request):
    jobs_list = Jobs.objects.filter(status ='active')
    context= {
        'jobs_list': jobs_list
    }
    return render(request,'lists-jobs/jobs.html',context)


def description(request, id):
    describe= Jobs.objects.get(pk=id)
    return render(request,'lists-jobs/describe.html',{'describe': describe})


def download(request, id):
    try:
        job = Jobs.objects.get(pk=id)
        file_path = job.description_file.path

        if job.description_file and os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
        else:
            raise Http404("File not found")
    except Jobs.DoesNotExist:
        raise Http404("Job not found")