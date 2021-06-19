from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.all().order_by('-users_who_like')

    context = {
        "posts": Post.objects.all().order_by("-created_at"),
        "trend_1":posts[0],
        "trend_2":posts[1],
        "trend_3":posts[2],
    }
    return render(request, 'index.html', context)

@login_required
def new_post(request):
    category = Category.objects.all()
    return render(request, 'new_post.html', {'category': category})
def new_post_form(request):
    if request.method == 'POST' and request.FILES['my_file']:
        user = User.objects.get(pk=request.POST['user_id'])
        category = Category.objects.get(id=request.POST['category'])
        post = Post.objects.create(title=request.POST['title'],description=request.POST['description'], image=request.FILES['my_file'], content=request.POST['content'],category=category, created_by=user)
        return redirect(f'/post/{post.id}')
    else:
        return redirect('/new_post')

def get_post(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'get_post.html', {'post':post})
@login_required        
def edit_post(request,id):
    post=Post.objects.get(id=id)
    return render(request, 'edit_post.html', {'post':post})
def edit_post_form(request):
    post = Post.objects.get(id=request.POST['post_id'])
    post.content=request.POST['content']
    post.title=request.POST['title']
    post.description=request.POST['description']
    post.save()
    return redirect(f"/post/{post.id}")

@login_required
def my_post(request):
    user = User.objects.get(pk=request.user.id)
    posts = user.user_posts.all()
    return render(request, 'my_post.html', {'posts':posts})

@login_required
def poster_profile(request,id):
    poster=User.objects.get(id=id)
    return render(request, 'poster.html', {'poster':poster})

@login_required
def delete_post(request,id):
    post =Post.objects.get(id=id)
    post.delete()
    return redirect('/')

def category(request,name):
    cat=Category.objects.get(name=name)
    return render(request,"category.html",{'cat':cat})

@login_required
def fav(request,id):
    post = Post.objects.get(id=id)
    user=User.objects.get(id=request.user.id)
    post.users_who_fav.add(user)
    return redirect(f"/post/{post.id}")
@login_required
def unfav(request,id):
    post = Post.objects.get(id=id)
    user=User.objects.get(id=request.user.id)
    post.users_who_fav.remove(user)
    return redirect(f"/post/{post.id}")
@login_required
def like(request,id):
    post = Post.objects.get(id=id)
    user=User.objects.get(id=request.user.id)
    post.users_who_like.add(user)
    return redirect(f"/post/{post.id}")
@login_required
def unlike(request,id):
    post = Post.objects.get(id=id)
    user=User.objects.get(id=request.user.id)
    post.users_who_like.remove(user)
    return redirect(f"/post/{post.id}")

@login_required
def my_fav(request):
    user = User.objects.get(id=request.user.id)
    posts=user.faves.all()
    return render(request,"my_fav.html",{'posts': posts})

@login_required
def comment_form(request):
    user = User.objects.get(id=request.user.id)
    post = Post.objects.get(id=request.POST['post_id'])
    if request.method =='POST':
        Comment.objects.create(text=request.POST['comment'],created_by=user,post_in=post)
        return redirect(f"/post/{post.id}")
    else:
        return redirect(f"/post/{post.id}")

@login_required
def delete_comment(request,id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect(f"/post/{comment.post_in.id}")