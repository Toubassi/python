from django.shortcuts import render, redirect
from .models import Dojo
from .models import Ninja


# Create your views here.
def index(request):
  dojos= Dojo.objects.all()
  context = {
    'dojos': dojos
  }
  return render(request, 'dojo.html', context)

def create_dojo(request):
  if request.method == 'POST':
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    Dojo.objects.create(name=name, city=city, state=state)
    return redirect('/list/')
  return redirect('/')

def add_ninja(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo = Dojo.objects.get(id=request.POST['dojo_id'])
    Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect('/list/')
  return redirect('/')

def list(request):
  dojos = Dojo.objects.all()
  ninjas = []
  for dojo in dojos:
    ninjas.append(Ninja.objects)
  context = {
    'dojos': dojos,
  }
  return render(request, 'list.html', context=context)
