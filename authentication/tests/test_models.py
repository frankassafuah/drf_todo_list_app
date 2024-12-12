from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('frank', 'frank@gmail.com', 'password')
        self.assertIsInstance(user, User) # checking if user is an instance of the User model
        self.assertEqual(user.email, 'frank@gmail.com') # checking if user email is the same as what we passed
        self.assertFalse(user.is_staff) # checking if user was not created as a superadmin

    def test_creates_super_user(self):
        user = User.objects.create_superuser('frank', 'frank@gmail.com', 'password')
        self.assertIsInstance(user, User) # checking if user is an instance of the User model
        self.assertEqual(user.email, 'frank@gmail.com') # checking if user email is the same as what we passed
        self.assertTrue(user.is_staff) # checking if user was created as a superadmin

    def test_raises_error_when_no_username_is_given(self):
        self.assertRaises(ValueError, User.objects.create_user, username='', email='frank@gmail.com', password='password')

    def test_raises_error_with_message_when_no_username_is_given(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='frank@gmail.com', password='password')

    def test_raises_error_when_no_email_is_given(self):
        self.assertRaises(ValueError, User.objects.create_user, username='frank', email='', password='password')

    def test_raises_error_with_message_when_no_email_is_given(self):
        with self.assertRaisesMessage(ValueError, "The given email must be set"):
            User.objects.create_user(username='frank', email='', password='password')
    
    def test_creates_super_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True'):
            User.objects.create_superuser(username='frank', email='frank@gmail.com', password='password', is_staff=False)
    
    def test_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='frank', email='frank@gmail.com', password='password', is_superuser=False)