from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
from django.shortcuts import render
from .models import Book # <-- Import your Book model

def index(request):
    books = Book.objects.all() # <-- Get all Book objects from the database
    context = {
        'books': books
    }
    return render(request, 'index.html', context) # <-- Pass the data to the template
from django.shortcuts import render, get_object_or_404 # <-- Add get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)

def detail(request, book_id): # <-- This is your new view
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book
    }
    return render(request, 'detail.html', context)
# Create your views here.
