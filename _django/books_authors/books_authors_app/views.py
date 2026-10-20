from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
  authors = Author.objects.all()
  books = Book.objects.all()
  context = {
    'authors': authors,
    'books': books
    }
  return render(request, 'add_author.html', context=context)

def add_book(request):
  if request.method == 'POST':
    Book.objects.create(
      title = request.POST['title'],
      desc = request.POST['desc']
    ) 
    return redirect('/add-book/')
  books = Book.objects.all()
  context = {
    'books':books,
  }
  return render(request, 'add_book.html', context)

def add_author(request):
  if request.method == 'POST':
    Author.objects.create(
      first_name = request.POST['first_name'],
      last_name = request.POST['last_name'],
      notes = request.POST['notes'],
    )
    return redirect('/')

def author_details(request, id):
  author = Author.objects.get(id=id)
  context = {
    'author' : author,
    'books': Book.objects.all(),
    'author_books': author.books.all()
  }
  return render(request, 'authors_details.html', context=context)

def book_details(request, id):
  book = Book.objects.get(id=id)
  context = {
    'book':book,
    'authors': Author.objects.all(),
  }
  return render(request, 'books_details.html', context=context)

def add_book_to_author(request, id):
    if request.method == 'POST':
        author = Author.objects.get(id=id)
        book = Book.objects.get(id=request.POST['book_id'])
        author.books.add(book)

    return redirect(f'/authors/{id}/')


def add_author_to_book(request, id):
    if request.method == 'POST':
        book = Book.objects.get(id=id)
        author = Author.objects.get(id=request.POST['author_id'])
        author.books.add(book)

    return redirect(f'/books/{id}/')