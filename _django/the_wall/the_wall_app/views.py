from django.shortcuts import render, redirect
from .models import Message, Comment
from login_reg.models import User
from login_reg.views import login, reg

# Create your views here.
def wall(request):
  if 'user_email' not in request.session:
    return redirect('/')
  
  email = request.session['user_email']
  for user in User.objects.all():
    if user.email == email:
      logged_user = user

  posts = Message.objects.all().order_by('-created_at')

  context = {'first_name': logged_user.first_name,
             'last_name': logged_user.last_name,
             'posts': posts,
             }
  return render(request, 'wall.html', context)

def post(request):
  if 'user_email' not in request.session:
      return redirect('/')
  
  email = request.session['user_email']
  for user in User.objects.all():
    if user.email == email:
      logged_user = user

  if request.method == 'POST':
    message = request.POST['message']
    Message.objects.create(message=message, user=logged_user)
    return redirect('/wall/')
  return render(request, 'wall.html')

def edit(request, id):
    if 'user_email' not in request.session:
      return redirect('/')

    email = request.session['user_email']
    for user in User.objects.all():
      if user.email == email:
        logged_user = user
    
    message = Message.objects.get(id=id)

    if message.user != logged_user:
      return redirect('/wall/')

    if request.method == 'POST':
      new_message = request.POST['edit_message']
      message.message = new_message
      message.save()
      return redirect('/wall/')
    
    context = { 'edit' : message }
    return render(request, 'edit.html', context)


def delete(request, id):
  if 'user_email' not in request.session:
    return redirect('/')
  
  email = request.session['user_email']
  for user in User.objects.all():
    if user.email == email:
      logged_user = user

  message = Message.objects.get(id=id)
  
  if message.user != logged_user:
    return redirect('/wall/')


  if request.method == 'POST':
    message.delete()
  return redirect('/wall/')
    

def comment(request, id):
  if 'user_email' not in request.session:
    return redirect('/')
  
  email = request.session['user_email']

  for user in User.objects.all():
    if user.email == email:
      logged_user = user

  message = Message.objects.get(id=id)

  if request.method == 'POST':
    comment_text = request.POST['comment']
    Comment.objects.create(comment=comment_text, user=logged_user, message=message)
  return redirect('/wall/')