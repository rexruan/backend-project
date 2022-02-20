"""
Test Cases for validators for the application of USER
"""
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import User
from ..validators import validate_password
from ..validators import validate_user_email
from ..validators import validate_username


class TestValidatePassword(TestCase):

    def test_validate_password_on_valid_password(self):
        short_valid_password = 'Passw0rd'
        self.assertEqual(validate_password(short_valid_password), None)
        long_valid_password = 'Aa10' * 8
        self.assertEqual(validate_password(long_valid_password), None)

    def test_validate_password_on_password_with_short_length(self):
        short_invalid_password = 'Pass123'
        self.assertRaises(
            ValidationError, 
            validate_password, 
            password=short_invalid_password
        )

    def test_validate_password_on_password_over_maximal_length(self):
        long_invalid_password = 'Aa1' * 11
        self.assertRaises(
            ValidationError,
            validate_password,
            password=long_invalid_password
        )
    
    def test_validate_password_on_password_without_number(self):
        password_without_number = 'Aa' * 8
        self.assertRaises(
            ValidationError,
            validate_password,
            password=password_without_number
        )
    
    def test_validate_password_on_password_without_uppercase(self):
        password_without_uppercase = 'a0' * 8
        self.assertRaises(
            ValidationError,
            validate_password,
            password=password_without_uppercase
        )
    
    def test_validate_password_on_password_without_lowercase(self):
        password_without_lowercase = 'A0' * 8
        self.assertRaises(
            ValidationError,
            validate_password,
            password=password_without_lowercase
        )

class TestValidateUserEmail(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        cls.example_user = User.objects.create(
            username="user1",
            password="Passw0rd1",
            email="example1@gmail.com"
        )
        
    
    def test_validate_user_email_on_valid_email(self):
        valid_email = 'user@gmail.com'
        self.assertEqual(validate_user_email(valid_email), None)
    
    def test_validate_user_email_on_invalid_email_format(self):
        invalid_email_without_at = 'usergmail.com'
        self.assertRaises(
            ValidationError,
            validate_user_email,
            email=invalid_email_without_at
        )

        invalid_email_without_valid_suffix = 'user@gmail'
        self.assertRaises(
            ValidationError,
            validate_user_email,
            email=invalid_email_without_valid_suffix
        )
    
    def test_validate_user_email_on_duplicate_email_address(self):
        
        self.assertRaises(
            ValidationError,
            validate_user_email,
            email=self.example_user.email
        )
    

class TestValidateUsername(TestCase):

    def test_validiate_username_on_valid_usernames(self):
        username = 'Username'
        self.assertEqual(validate_username(username), None)
        
        valid_username_with_minimal_length = 'un'
        self.assertEqual(
            validate_username(valid_username_with_minimal_length),
            None
        )

        valid_username_with_maximal_length = 'username' * 16 
        self.assertEqual(
            validate_username(valid_username_with_maximal_length),
            None
        )
    
    def test_validate_username_on_invalid_usernames(self):
        invalid_short_username = 'n'
        self.assertRaises(
            ValidationError,
            validate_username,
            username=invalid_short_username
        )
        
        invalid_long_username = 'Username' * 16 + '!'
        self.assertRaises(
            ValidationError,
            validate_username,
            username=invalid_long_username
        )
