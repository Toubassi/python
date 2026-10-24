from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import UserManager, User

# Create your views here.
def register(request):
  if request.method == 'POST':
    errors = User.objects.validator(request.POST)
    if errors:
      for key, value in errors.items():
        messages.error(request, value)
      return redirect('/')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    bday = request.POST['bday']
    password = request.POST['password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name=first_name, last_name=last_name, email=email, bday=bday, password=hashed_pw)
    request.session['user_email'] = user.email
    return redirect('/home/')
  return render(request, 'index.html')

def success(request):
  if request.method == 'POST':
    try: 
      user = User.objects.get(email = request.POST['email'])
      if user:
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
          request.session['user_email'] = user.email
          return redirect('/home/')
    except:
      messages.error(request, f"The email: {request.POST['email']} that you entered does not exist.")
      return redirect('/success/')
    return redirect('/')
  return render(request, 'index.html')

def home(request):
  email = request.session.get('user_email')
  if not email:
    return redirect('/')
  user = None
  for my_user in User.objects.all():
    if my_user.email == email:
      user = my_user
  if user is None:
    request.session.flush()  
    return redirect('/')
  return render(request, 'success.html', {'user': user})
  

def logout(request):
    request.session.flush()  
    return redirect('/')
