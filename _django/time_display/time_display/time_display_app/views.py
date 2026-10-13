from django.shortcuts import render
from time import gmtime, localtime, strftime

# Create your views here.
def index(request):
  context = {
    "date": strftime("%H:%M", localtime()),
    "time": strftime("%Y-%m-%d", localtime()),
    }
  return render(request, 'index.html', context)