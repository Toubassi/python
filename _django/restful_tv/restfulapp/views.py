from django.shortcuts import render, redirect
from .models import Tv_Show
# Create your views here.
def index(request):
  shows = Tv_Show.objects.all()
  context = {
      'shows': shows,
    }

  return render(request, 'all_shows.html', context)

def create(request):
  if request.method == 'POST':
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    desc = request.POST['desc']
    show= Tv_Show.objects.create(
      title = title,
      network = network,
      release_date = release_date,
      desc = desc,
    )
    return redirect(f'/shows/{show.id}/')
  show = Tv_Show.objects.all()
  context = {
  'show': show,
    }
  return render(request, 'index.html', context=context)

def the_show(request, id):
  show = Tv_Show.objects.get(id=id)
  context= {
      'show': show,
    }
  return render(request, 'shows.html', context)


def destroy(request, id):
  show = Tv_Show.objects.get(id=id)
  show.delete()
  return redirect('/')

def update(request, id):
  show = Tv_Show.objects.get(id=id)
  if request.method =='POST':
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.desc = request.POST['desc']
    show.save()

    return redirect(f'/shows/{show.id}/')
  return render(request, 'update.html', {"show": show})