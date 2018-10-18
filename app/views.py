from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    '''
    returns the homepage of the application
    '''
    residence = Hood.objects.all
    return render(request, 'index.html', {'content': residence})

@login_required(login_url='/accounts/login/')
def profile(request,name):
    human = Resident.get_human(jina=name)

    return render(request, 'profile.html', {'content': human})
