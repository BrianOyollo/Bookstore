from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm


# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        test_user = User.objects.create_user(username='Harvey', email='harvey@gmail.com', password='specter12345')
        self.assertEqual(test_user.username, 'Harvey')
        self.assertEqual(test_user.email, 'harvey@gmail.com')
        self.assertTrue(test_user.is_active)
        self.assertFalse(test_user.is_staff)
        self.assertFalse(test_user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        test_admin = User.objects.create_superuser(username='admin', email='admin@gmail.com', password='storeadmin')
        self.assertEqual(test_admin.username, 'admin')
        self.assertEqual(test_admin.email, 'admin@gmail.com')
        self.assertTrue(test_admin.is_active)
        self.assertTrue(test_admin.is_staff)
        self.assertTrue(test_admin.is_superuser)


class SignUpTest(TestCase):
    username = 'newuser'
    email = 'newuser@gmail.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def TestSignupTemplate(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, 'you are logged in!')

    def test_signup_template(self):
        user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
