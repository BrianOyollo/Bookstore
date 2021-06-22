from django.test import TestCase
from django.contrib.auth import get_user_model


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
