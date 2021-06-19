from django.shortcuts import render, redirect
# from django.utils.datastructures import MultiValueDictKeyError
# try:
#     is_private = request.POST['is_private']
# except MultiValueDictKeyError:
#     is_private = False
# if 'is_private' in request.POST:
#     is_private = request.POST['is_private']
# else:
#     is_private = False

def index(request):
    return render(request,"index.html")

def result(request):
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']
    context = {
    	"name_on_template" : name_from_form,
    	"location_on_template" : location_from_form,
        "language_on_template" : language_from_form,
        "comment_on_template" : comment_from_form
    }
    return render(request,"show.html",context)
    # return redirect("/success")

# def success(request):
#     # this is the success route
#     return render(request,"show.html",context)    