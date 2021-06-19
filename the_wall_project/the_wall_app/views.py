from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime
# Create your views here.

def index(request):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        messages = Messages.objects.all()   
        return render(request,'home.html', {'user': user, 'messages':messages})
    else:
        return redirect("/login")
def login(request):
    return render(request,'login.html')
def login_form(request):
    if 'user' in request.session:
        return redirect("/")
    else:
        if request.method=="POST":
            user=User.objects.filter(email=request.POST['email'])
            if user:
                logged_user = user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                    request.session['user'] = logged_user.id
                    messages.success(request,"Successfully logged in")
                    return redirect("/")
                else:
                    messages.error(request,"Email or password is not correct")
                    return redirect("/login")
            else:
                messages.error(request,"Email or password is not correct")
                return redirect("/login")
def register(request):
    if 'user' in request.session:
        return redirect("/")
    if 'errors' in request.session:
        return render(request,'register.html', {'errors': request.session['errors']})
    else:
        request.session['errors'] = {}
        return redirect("/register")
def register_form(request):
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        request.session['errors'] = errors
        print(request.session['errors'])
        for key,val in errors.items():
            messages.error(request,val)
        return redirect("/register")
    else:
        if request.method=="POST":
            password=request.POST['password']
            passHash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
            newUser = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],
            password=passHash)
            request.session['user'] = newUser.id
            del request.session['errors']
            messages.success(request,"User successfully created")
        return redirect("/")
def logout(request):
    request.session.flush()
    return redirect("/")
def create_message(request):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user'])
        Messages.objects.create(message=request.POST['message'],user_id=user)
        return redirect("/")
    else:
        return redirect("/")

#  wall 
def wall(request):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        messages = Messages.objects.all()   
        return render(request,'wall.html', {'user': user, 'messages':messages})
    else:
        return redirect("/")
def create_comment(request, id):
    if request.method == 'POST':
        message = Messages.objects.get(id=id)
        user = User.objects.get(id=request.session['user'])
        Comments.objects.create(comment=request.POST['comment'], user_id=user, message_id= message)
        return redirect("/wall")
    else:
        return redirect("/wall")

def delete_message(request, id):
    message = Messages.objects.get(id=id)
    date_created=message.created_at.date()
    tody = datetime.today().date()
    if tody == date_created:
        created_hour = message.created_at.timestamp()
        minute = datetime.today().timestamp()
        result = minute - created_hour
        if int(result) < 1800:
            message.delete() 
    return redirect("/")
    