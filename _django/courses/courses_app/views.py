from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CourseManager, Course, Description 

# Create your views here.
def index(request):
  courses = Course.objects.all()
  desc = Description.objects.all()
  context = {
    'courses': courses,
    'desc': desc,
  }
  return render(request, 'index.html', context)

def create(request):
  if request.method =='POST':
    errors = Course.objects.basic_validator(request.POST)
    if errors:
      for key, value in errors.items():
        messages.error(request, value)
      return redirect('/')
    name = request.POST['the_course']
    description = request.POST['the_description']
    course = Course.objects.create(the_course=name)
    Description.objects.create(the_description=description, course=course)
    return redirect('/')
  return render(request, 'index.html')

def confirm(request, id):
  course = Course.objects.get(id=id)
  desc = course.description.the_description
  context = {
    'course': course,
    'desc': desc,
  }
  return render(request, 'destroy.html', context)

def destroy(request, id):
  course = Course.objects.get(id=id)
  course.delete()
  return redirect('/')