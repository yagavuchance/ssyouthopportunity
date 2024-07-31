from django.shortcuts import render
from .models import Scholarship

# Create your views here.

def scholarship(request):
    scholarship_list = Scholarship.objects.all()
    context= {
        'scholarship_list': scholarship_list
    }
    return render(request, 'scholars/scholarships.html',context)
