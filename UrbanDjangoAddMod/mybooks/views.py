from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Book


def books_list(request):
    books = Book.objects.all().order_by('-id')
    paginator = Paginator(books, 3)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {'books': books}
    return render(request, 'book_list.html', context)


def books_list_view(request):
    per_page = request.GET.get('per_page') or 2
    books = Book.objects.all().order_by('-id') or per_page
    paginator = Paginator(books, per_page)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {'books': books}
    return render(request, 'book_list_view.html', context)

