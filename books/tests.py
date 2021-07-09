from django.http import response
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from .models import Book, Review
from django.contrib.auth import get_user_model

# Create your tests here.


class BookTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='reviewuser',
            email='reviewuser@gmail.com',
            password='testuser12345'
        )
        self.book = Book.objects.create(
            title='The Broker',
            author='John Grisham',
            price='10.00',
        )
        self.review = Review.objects.create(
            author=self.user,
            book=self.book,
            review='Nice book.',
        )

    def test_new_user(self):
        self.assertEqual(self.user.username, 'reviewuser')
        self.assertEqual(self.user.email, 'reviewuser@gmail.com')

    def test_book_listing(self):
        self.assertEqual(self.book.title, 'The Broker')
        self.assertEqual(self.book.author, 'John Grisham')
        self.assertEqual(self.book.price, '10.00')

    def test_book_review(self):
        self.assertEqual(self.review.review, 'Nice book.')
        self.assertEqual(self.review.author.username, 'reviewuser')
        self.assertEqual(self.review.book.title, 'The Broker')

    def test_book_list_view(self):
        self.response = self.client.get(reverse('book-list'))
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, 'The Broker')
        self.assertNotContains(self.response, 'Reviews')
        self.assertTemplateUsed(self.response, 'books/book_list.html')

    def test_book_detail_view(self):
        self.response = self.client.get(self.book.get_absolute_url())
        self.wrong_response = self.client.get('/books/1')
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.wrong_response.status_code, 404)
        self.assertContains(self.response, 'John Grisham')
        self.assertContains(self.response, 'Nice book.')
        self.assertContains(self.response, 'The Broker')
        self.assertNotContains(self.response, 'Add to cart')
        self.assertTemplateUsed(self.response, 'books/book_detail.html')
