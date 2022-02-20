

from django.db import models

# Create your models here.
class User(models.Model):

    class Meta:

        app_label = 'user'
    
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username


