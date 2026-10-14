from django.shortcuts import render, redirect
import random


# Create your views here.
def index(request):
  guess = 0
  message = request.session.pop('message', "")
  if 'attempts' not in request.session:
    request.session['attempts'] = 0
  if 'the_number' not in request.session:
    request.session['the_number'] = random.randint(1, 100)
  if request.method == "POST":
    guess = int(request.POST['guess'])
    if request.session['the_number'] > guess:
      message = "Your number is too low"
      request.session['attempts'] +=1
    elif request.session['the_number'] < guess:
      message = "Your number is too high"
      request.session['attempts'] +=1
    else: 
      request.session['attempts'] +=1
      message = f"Correct! You got it in {request.session['attempts']} attempts!"
      request.session['message'] = message
      return redirect('/')
  attempts = request.session['attempts']
  return render(request, 'index.html', {'guess': guess, 'message': message, 'attempts': attempts})

def clear(request):
  request.session.flush()
  return redirect('/')