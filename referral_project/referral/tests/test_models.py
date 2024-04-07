from django.test import TestCase
from django.utils import timezone
from referral.models import CustomUser 

class CustomUserModelTest(TestCase):
    def test_user_creation(self):
        # Create a user with specific attributes
        username = 'testuser'
        email = 'test@example.com'
        password = 'password123'
        user = CustomUser.objects.create_user(username=username, email=email, password=password)

        # Assert user attributes
        self.assertEqual(user.username, username)  # Check username
        self.assertEqual(user.email, email)        # Check email
        self.assertTrue(user.check_password(password))  # Check password
        self.assertIsNone(user.referral_code)      # Check referral_code is None
        self.assertIsNone(user.referral_by)        # Check referral_by is None

        # Check registration_date is within 1 second of current time
        self.assertTrue(timezone.now() - user.registration_date < timezone.timedelta(seconds=1))



# class CustomUserModelTest(TestCase):
#     def test_user_creation(self):
#         user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='password123')
#         self.assertEqual(user.username, 'testuser')
#         self.assertEqual(user.email, 'test@example.com')
#         self.assertTrue(user.check_password('password123'))
#         self.assertIsNone(user.referral_code)
#         self.assertIsNone(user.referral_by)
#         self.assertTrue(timezone.now() - user.registration_date < timezone.timedelta(seconds=1))
