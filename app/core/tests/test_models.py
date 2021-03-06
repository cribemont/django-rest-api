from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """ Test user creation with email """
        email = 'test@google.com'
        password = 'azerty123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test new user email normalised """
        email = 'test@GOOGlE.COM'
        user = get_user_model().objects.create_user(email, 'azerty123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'azerty123')

    def test_create_superuser(self):
        """ Test creating superuser """
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test12343'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
