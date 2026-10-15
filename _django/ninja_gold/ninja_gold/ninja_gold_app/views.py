from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = []

    return render(request, 'index.html', {
        'gold': request.session['gold'],
        'activities': request.session['activities']
    })


def process_money(request):
    if request.method != 'POST':
        return redirect('/')

    if 'gold' not in request.session:
        request.session['gold'] = 0 
    
    if 'activities' not in request.session:
        request.session['activities'] = []
    
    building = request.POST.get('building')
    earned = 0
    if building == 'farm':
        earned = random.randint(1, 5)
    elif building == 'cave':
        earned = random.randint(6, 10)
    elif building == 'house':
        earned = random.randint(11, 20)
    elif building == 'quest':
        earned = random.randint(-50, 50)

    request.session['gold'] += earned

    if earned >= 0:
        activity = f"Earned {earned} gold from the {building}"
        
    else:
        activity = (
            f"Entered the casino and lost {abs(earned)} gold"
        )

    activities = request.session['activities']
    activities.insert(0, activity)
    request.session['activities'] = activities

    return redirect('/')


def clear(request):
    request.session.flush()
    return redirect('/')
