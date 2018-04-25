from django.shortcuts import render, get_object_or_404
from .models import Book


def index(request):
    context = {}
    book_list = Book.objects.all()
    context['book_list'] = book_list
    return render(request, 'index.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {}
    context['book'] = book
    return render(request, 'core/book_detail.html', context)
