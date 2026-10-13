from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if 'number' not in request.session:
        request.session['number'] = 0
    elif 'number' in request.session:
        request.session['number'] += 1

    return render(request, 'index.html')

def decrease(request):
    if 'number' not in request.session:
        request.session['number'] = 0
    elif 'number' in request.session:
        request.session['number'] -= 2

    return redirect('/')

def clear(request):
    request.session.flush()
    return redirect('/')