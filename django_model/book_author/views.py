from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from .forms import AuthorForm, BookForm
from .models import Author, Book

def list_all_books(request):
    context = {}
    context['books'] = Book.objects.all()
    return render(request, "book_author/home.html", context)

def list_authors(request):
    context = {}
    context['authors'] = Author.objects.all()
    return render(request, "book_author/author_list.html", context)

def register_author(request):
    if request.method == "GET":
        context = {}
        form = AuthorForm(None)
        context['form'] = form
        return render(request, "book_author/registeration_form.html", context)
    else:
        context = {}
        form = AuthorForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
        return redirect('/authors')

def regiter_book(request):
    if request.method == "GET":
        context = {}
        form = BookForm(None)
        context['form'] = form
        return render(request, "book_author/registeration_form.html", context)
    else:
        context = {}
        form = BookForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
        return redirect('/')
