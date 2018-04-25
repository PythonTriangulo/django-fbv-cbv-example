from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Book
from .forms import BookForm


def home(request):
    return HttpResponse('<h1>Bookstore</h1>')


def index(request):
    context = {}
    book_list = Book.objects.all()
    context['book_list'] = book_list
    return render(request, 'index.html', context)


class Index(View):

    def get(self, request):
        context = {}
        book_list = Book.objects.all()
        context['book_list'] = book_list
        return render(request, 'index.html', context)


class BookList(TemplateView):
    model = Book
    template_name = 'core/book_list.html'

    def get_context_data(self, **kwargs):
        context = {}
        book_list = Book.objects.all()
        context['book_list'] = book_list
        return context


class BookList(ListView):
    model = Book
    template_name = 'core/book_list.html'
    context_object_name = 'book_list'


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {}
    context['book'] = book
    return render(request, 'core/book_detail.html', context)


class BookDetail(DetailView):
    model = Book
    template_name = 'core/book_detail.html'
    context_object_name = 'book'


def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:book_list')
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'core/book_add.html', context)


class BookCreate(CreateView):
    model = Book
    template_name = 'core/book_add.html'
    form_class = BookForm
