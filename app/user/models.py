import re

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

def validate_username(username):
    print('user_name', username)
    if len(username) < 2 or len(username) > 128:
        raise ValidationError(
            _(f'{username} is expected to have at least two characters, but no more than 128 characters'),
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
        r'(?=.*[0-9])'
        r'(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'.{8, 32}'
    )
    if not password_re.fullmatch(password):
        raise ValidationError(
            _(f'The length of password is betweeen 8 and 32;\n\
                Password contains number, uppercase and lowercase'),
            params = {'password': password}
        )


class User(models.Model):

    class Meta:

        app_label = 'user'
    
    username = models.CharField(max_length=128, validators=[validate_username])
    password = models.CharField(max_length=32, validators=[validate_password])
    email = models.EmailField(
        max_length=254,
        blank=False,
        unique=True,
        validators=[validate_email]
    )

    def __str__(self):
        return self.username


