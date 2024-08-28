from django.shortcuts import render,redirect
from jobs.models import Jobs
from scholarship.models import Scholarship
from fellowships.models import Fellowship
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    jobs_list = Jobs.objects.filter(status ='active').order_by('-created_at')
    scholarship_list = Scholarship.objects.all()[:4]
    fellowship_list = Fellowship.objects.all()[:5]
    context= {
        'jobs_list': jobs_list,
        'scholarship_list': scholarship_list,
        'fellowship_list': fellowship_list
    }
    return render(request,'cores/index.html',context)

def about(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            message = form.cleaned_data['message']

            # Construct email content
            subject = f"inquiry from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send email
            send_mail(
                subject,
                body,
                email,  # Sender's email
                [settings.DEFAULT_TO_EMAIL],  # Your email
                fail_silently=False,
            )
             # Add success message
            messages.success(request, 'Your message has been sent successfully. Thank you for contacting us!')

            # Redirect to a success page or render a success message
            return redirect('success')  # Replace 'success' with the appropriate view name or URL

    else:
        form = ContactForm()

        return render(request, 'cores/about.html', {'form': form})

def success(request):
    return render(request, 'cores/sent-success.html')  # Render the success template


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


def robots_txt(request):
    content = render_to_string('cores/robots.txt')
    return HttpResponse(content, content_type='text/plain')

  