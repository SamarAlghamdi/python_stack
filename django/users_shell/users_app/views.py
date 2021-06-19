from django.shortcuts import render, redirect
from .models import Users

# Create your views here.
def index(request):
    users=Users.objects.all()
    return render(request,"index.html",{"users":users})

def add(request):
    if request.method=="POST":
        newUser=Users.objects.create(first_name=request.POST["first-name"],last_name=request.POST["last-name"],email_address=request.POST["email"],
        age=request.POST["user_age"])
        newUser.save()
        return redirect("/")
        
