"""
Customized validators
"""
import re

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

from user.models import User

def validate_username(username):
    """doc string"""
    if len(username) < 2 or len(username) > 128:
        raise ValidationError(
            _(f'{username} is expected to have at least two characters, '
                'but no more than 128 characters'),
            params = {'username': username}
        )

def validate_password(password):
    """
    password is valid iff
    1. consisting of 8 characters
    2. no more than 32 characters
    2. having at least a capital letter, a small letter and a number
    """
    password_re = re.compile(
        r'^'
        r'(?=.*\d)'
        r'(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'.{8,32}'
        r'$'
    )
    if not password_re.fullmatch(password):
        raise ValidationError(
            'The length of password is between 8 and 32;'
            'Password contains number, uppercase and lowercase.',
            params = {'password': password}
        )

def validate_user_email(email, update=False):
    """customized email validator"""
    # if compatible with email format
    validate_email(email)
    # if email does exist in the database
    if not update:
        if email in User.objects.all().values_list('email', flat=True):
            raise ValidationError(
                _('The email has been registered'),
                params = {'email': email}
            )
  