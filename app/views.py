from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def new_resident(request, operation, name):
    current_user = request.user
    hood = get_object_or_404(Hood, name=name)
    home = Hood.get_hood(jina=name)
    if request.method == 'POST':
        form = NewResidentForm(request.POST, request.FILES)
        if form.is_valid():
            resident = form.save(commit=False)
            resident.name = current_user
            resident.home = hood
            resident.save()
        return redirect('home')
    else:
        form = NewResidentForm()

    if operation == 'join':
        hood.occupants +=1
        hood.save()

    return render(request, 'new_being.html', {'form': form, 'content': home})

@login_required(login_url='/accounts/login/')
def residence(request,jina):
    area = Hood.get_hood(jina=jina)
    service = Service.get_service(jina=jina)

    return render(request, 'area.html', {'content': area, 'addon': service, 'title': area})
