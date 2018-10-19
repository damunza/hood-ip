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
    news = Event.get_event(jina=jina)

    return render(request, 'area.html', {'content': area, 'addon': service, 'news':news})

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

@login_required(login_url='/accounts/login/')
def new_business(request,jina):
    current_user = request.user
    home = Hood.get_hood(jina=jina)
    area = get_object_or_404(Hood, name=jina)
    if request.method == 'POST':
        form = NewBusiness(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = current_user
            business.neighbourhood = area
            business.save()

        return redirect('home')

    else:
        form = NewBusiness()

    return render(request, 'bizna.html', {'form': form, 'content': home})

@login_required(login_url='/accounts/login/')
def new_service(request,jina):
    home = Hood.get_hood(jina=jina)
    area = get_object_or_404(Hood, name=jina)
    if request.method == 'POST':
        form = NewService(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.area = area
            service.save()

        return redirect('home')

    else:
        form = NewService()

    return render(request, 'service.html', {'form': form, 'content': home})

@login_required(login_url='/accounts/login/')
def new_event(request,jina):
    home = Hood.get_hood(jina=jina)
    area = get_object_or_404(Hood, name=jina)
    if request.method == 'POST':
        form = NewEvent(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.area = area
            event.save()

        return redirect('home')

    else:
        form = NewEvent()

    return render(request, 'event.html', {'form': form, 'content': home})

@login_required(login_url='/accounts/login/')
def new_hood(request):
    if request.method == 'POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()

        return redirect('home')

    else:
        form = NewHoodForm()

    return render(request, 'pop.html', {'form': form})
