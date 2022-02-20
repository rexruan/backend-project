"""
"""
from django.test import TestCase

from ..models import User
# Create your tests here.

class UserTestCase(TestCase):
    
    def test_users_creation(self):
        User.objects.create()
    

    def test_model_str(self):
        user = User.objects.create(
            username='Eriksson',
            password='Passw0rd',
            email='email@example.se'
        )
        
        self.assertEqual(str(user), "Eriksson")