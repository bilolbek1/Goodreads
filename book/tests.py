from django.test import TestCase
from django.urls import reverse

from book.models import Book


class BookTestCase(TestCase):
    def test_list(self):
        response = self.client.get(reverse('list'))

        self.assertContains(response, 'There is no Books.')

    def test_list_title(self):
        Book.objects.create(title='Bolaligim', description='Description1', isbn='12345678')
        Book.objects.create(title='Alpomish', description='Description2', isbn='12122121')
        Book.objects.create(title='Xamza', description='Description3', isbn='1234545565')
        Book.objects.create(title='Ikki eshik orasi', description='Description4', isbn='12786544')

        response = self.client.get(reverse('list'))

        books = Book.objects.all()

        for i in books:
            self.assertContains(response, i.title)

    def test_detail(self):
        book = Book.objects.create(title='Oq kema', description='Description1', isbn='1212121')

        response = self.client.get(reverse('detail', kwargs={"id": book.id}))

        self.assertContains(response, book.title.upper())
        self.assertContains(response, book.description.upper())
        self.assertContains(response, book.isbn)




























































































