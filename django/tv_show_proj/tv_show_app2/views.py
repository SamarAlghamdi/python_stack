from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return redirect("/shows")

def shows(request):
    context={
        "all_shows":Show.objects.all(),
    }
    return render(request,"show.html",context)
def new(request):
    context={
        "networks":Network.objects.all(),
    }
    return render(request,"create.html",context)
def create(request):
    errors=Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, val in errors.items():
            messages.error(request,val)
        return redirect("/shows/new")
    else:
        if request.method=="POST":
            new_show=Show.objects.create(title=request.POST['title'],release_date=request.POST['date']
            ,network=Network.objects.create(name=request.POST['select_network']),desc=request.POST['desc'])
            messages.success(request,'Show successfully created!')
        return redirect(f"/shows/{new_show.id}")
def read(request,id):
    context={
        "show":Show.objects.get(id=id),
    }
    return render(request,"read.html",context)
def edit(request,id):
    context={
        "show":Show.objects.get(id=id),
        # "networks":Network.objects.exclude(id=id),
    }
    return render(request,"update.html",context)
def update(request,id):
    errors=Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, val in errors.items():
            messages.error(request,val)
        return redirect(f"/shows/{id}/edit")
    else:
        if request.method=="POST":
            show=Show.objects.get(id=id)
            show.title=request.POST['title']
            show.release_date=request.POST['date']
            if request.POST['select_network'] in Network.objects.all():
                show.network=Network.objects.get(name=request.POST['select_network'])
            else:
                newNet=Network.objects.create(name=request.POST['select_network'])
                show.network=newNet
            show.desc=request.POST['desc']
            show.save()
        return redirect(f"/shows/{show.id}")
def delete(request,id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect("/shows")