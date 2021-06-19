from django.shortcuts import render

# Create your views here.
def root(request):
    return HttpResponse("/blogs")
from django.shortcuts import HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
