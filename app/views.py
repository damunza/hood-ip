from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    '''
    returns the homepage of the application
    '''
    return render(request, 'index.html')
