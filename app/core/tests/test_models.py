from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from core import models

def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
            """Test  creating a new user wth email is successful"""
            email = "gopal@gmail.com"
            password = "abc123"
            user = get_user_model().objects.create_user(
                email=email,
                password=password
            )

            self.assertEqual(user.email, email)
            self.assertTrue(user, check_password(self, password))

    def test_new_user_email_normalized(self):
        email = "gopal@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "abc123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'abc123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'gopal@gmail.com', 'test@123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
