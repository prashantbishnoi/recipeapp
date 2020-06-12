from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'abc@abc.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test email for a new user is normalized"""
        email = 'abc@ABC.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_no_email(self):
        """Test creating a new user without an email is unsuccessful"""
        password = 'test123'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password=password
            )

    def test_create_superuser_successful(self):
        """Test creating a new super user is successful"""
        email = 'abc@abc.com'
        password = 'test123'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
