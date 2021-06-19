from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process_money(request):
    date = strftime("%Y-%m-%d %H:%M %p", gmtime())
    if 'gold' in request.session:
        print(request.session['gold'])
        if "farm" in request.POST:
            request.session['gold'].append({"value":f"Earned {random.randint(10,20)} golds from the farm! {date}", "color":"green"})
        elif "cave" in request.POST:
            request.session['gold'].append({"value":f"Earned {random.randint(5,10)} golds from the cave! {date}", "color":"green"})
        elif 'house' in request.POST:
            request.session['gold'].append({"value":f"Earned {random.randint(2,5)} golds from the house! {date}", "color": "green"})
        elif 'casino' in request.POST:
            request.session['gold'].append({"value":f"Earned a casino and lost {random.randint(5,10)} golds ...Ouch!! {date}", "color":"red"})
        request.session.save()
    else:
        request.session['gold'] = [{}]        
    return redirect('/')

