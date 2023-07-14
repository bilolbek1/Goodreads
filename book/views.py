from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from book.models import Book


class BookListView(View):
    def get(self, request):
        book_list = Book.objects.all()
        context = {
            'book_list': book_list
        }
        return render(request, 'books_list.html', context=context)

class BookDetailView(View):
    def get(self, request, id):
        book_detail = Book.objects.get(id=id)
        context = {
            'book_detail': book_detail
        }
        return render(request, 'book_detail.html', context=context)
















































