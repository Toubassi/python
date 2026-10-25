from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from django.contrib import messages
from .models import UserManager, User

# Create your views here.
def login(request):
  if request.method == 'POST':
    try:
      user = User.objects.get(email = request.POST['email'])
      if user:
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
          request.session['user_email'] = user.email
          return redirect('/wall/')
    except:
      messages.error(request, f"email or password is incorrect")
      return redirect('/')
  return render(request, 'login.html')

def reg(request):
  if request.method == 'POST':
    errors = User.objects.validator(request.POST)
    if errors:
      for key, value in errors.items():
        messages.error(request, value)
      return redirect('/reg/')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name=first_name, last_name=last_name, email = email, password=hashed_pw)
    request.session['user_email'] = user.email
    return redirect('/wall/')
  return render(request, 'registration.html')

def logout(request):
  request.session.flush()  
  return redirect('/')