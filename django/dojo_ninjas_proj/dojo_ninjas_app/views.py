from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context ={
        "all_dojos":Dojos.objects.all()
    }
    return render(request,"index.html",context)

def add_dojo(request):
    if request.method=="POST":
        newDojo = Dojos.objects.create(name=request.POST["name"],city=request.POST["city"],state=request.POST["state"])
    return redirect("/")

def add_ninja(request):
    if request.method=="POST":
        newNinja = Ninjas.objects.create(dojo_id=Dojos.objects.get(id=request.POST["dojo"]),first_name=request.POST["first-name"], last_name=request.POST["last-name"])
    return redirect("/")

def delete_dojo(request,id):
    dojo=Dojos.objects.get(id=id)
    dojo.delete()
    return redirect("/")
