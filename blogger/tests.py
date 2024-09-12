from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LoginTest(TestCase):
    def setUp(self):
        # Create a user to test login
        self.username = 'testuser'
        self.password = 'testpassword'
        User.objects.create_user(
            username=self.username, password=self.password)

    def test_login_success(self):
        # Test logging in with correct credentials
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('home'))
        # Adjust 'home' to the actual success URL

    def test_login_failure(self):
        # Test logging in with incorrect credentials
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Stay on the login page
        self.assertContains(response, 'Invalid username or password')

    def test_login_empty_fields(self):
        # Test submitting the form without any credentials
        response = self.client.post(reverse('login'), {
            'username': '',
            'password': ''
        })
        self.assertEqual(response.status_code, 200)
        # Stay on the login page
        self.assertContains(response, 'This field is required.', count=2)
        # Ensure form errors appear
