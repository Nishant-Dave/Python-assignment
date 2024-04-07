from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from referral.models import CustomUser

class UserRegistrationAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        url = reverse('register')
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'testuser')


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        url = '/api/'
        data = {
            'name': 'Dexter',
            'email': 'Dexter@email.com',
            'password': 'Password123'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)  


        user = CustomUser.objects.get(email='dexter@email.com')
        self.assertEqual(user.name, 'Dexter')
        self.assertEqual(user.email, 'johndoe@example.com')


class UserDetailsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.token = self.user.get_token()

    def test_user_details(self):
        url = '/api/user/'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.data['email'], 'test@example.com')  
        

class ReferralsEndpointTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='referrer', email='referrer@example.com', password='password123')
        self.referred_user = CustomUser.objects.create_user(username='referred', email='referred@example.com', password='password456')
        self.user.referral_code = 'REFERRAL123'
        self.user.save()
        self.referred_user.referral_by = self.user
        self.referred_user.save()
        self.token = self.user.get_token()

    def test_user_referrals(self):
        url = '/api/referrals/'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(len(response.data['results']), 1)  
        referred_user_data = response.data['results'][0]
        self.assertEqual(referred_user_data['email'], 'referred@example.com')  
        