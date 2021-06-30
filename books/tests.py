from django.http import response
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from .models import Book

# Create your tests here.


class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title='The Broker',
            author='John Grisham',
            price='9.99'
        )

    def test_book_listing(self):
        self.assertEqual(self.book.title, 'The Broker')
        self.assertEqual(self.book.author, 'John Grisham')
        self.assertEqual(self.book.price, '9.99')

    def test_booklistview(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Broker')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_BookDetailView(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('books/1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Broker')
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'books/book_detail.html')
