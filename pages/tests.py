from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class HomepageTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse('homepage')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contain_correct_html(self):
        self.assertContains(self.response, '')

    def test_homepage_doesnt_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'hello there')


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('aboutpage')
        self.response = self.client.get(url)

    def test_about_page(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'about.html')
        self.assertContains(self.response, 'About')

