from django.shortcuts import render, redirect
from .forms import JobForm, ScholarshipForm
from jobs.models import Jobs
from django.contrib import messages

# Create your views here.

def Jobpost(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            messages.success(request, f'job posted successfully')
            return redirect('login_success')
            
    else:
         form = JobForm()
    return render(request, 'posts/post-jobs.html',{'form':form})

def scholarshippost(request):
    if request.method == "POST":
        form = ScholarshipForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            messages.success(request, f'scholarship posted successfully')
            return redirect('login_success')
            
    else:
         form = ScholarshipForm()
    return render(request, 'posts/post-scholars.html',{'form':form})

def post_success(request):
    return render(request, 'posts/posts_success.html')

def edit_success(request):
    return render(request, 'posts/posts_success.html')


def view_post(request, id):
    post_view = Jobs.objects.get(pk=id)
    context ={
        'post_view': post_view
    }
    return render(request,'posts/view-post.html', context)

def edit(request, id):
    job= Jobs.objects.get(pk=id)
    if request.method == "POST":
        form = JobForm(request.POST,  request.FILES, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record Updated successfully')
            return redirect('edit_success')
    else:
        form = JobForm(instance=job)
    return render(request,'posts/edit.html',{'form':form})

def delete(request, id):
    form= Jobs.objects.get(pk=id)
    form.delete()
    return redirect('E-dashboard')

def status(request, id):
    job= Jobs.objects.get(pk=id, created_by=request.user)
    if job.status == 'active':
        job.status ='inactive'
    else:
        job.status = 'active'
    job.save()
    return redirect('E-dashboard')