"""
"""
from django.test import TestCase

from ..models import User
# Create your tests here.

class UserTestCase(TestCase): 

    def test_model_str(self):
        user = User.objects.create(
            username='username',
            password='Passw0rd',
            email='email@example.se'
        )
 
        self.assertEqual(str(user), "username")
