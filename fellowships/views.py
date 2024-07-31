from django.shortcuts import render
from .models import Fellowship

# Create your views here.

def fellowship(request):
    fellowship_list = Fellowship.objects.all()
    context= {
        'fellowship_list': fellowship_list
    }
    return render(request, 'fellow/fellowships.html',context)
