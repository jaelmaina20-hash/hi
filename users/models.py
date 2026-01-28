from django.db import models
from django.contrib.auth.models import User
from encrypted_model_fields.fields import EncryptedCharField, EncryptedTextField

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    ssn = EncryptedCharField(max_length=11)
    bio = EncryptedTextField()

    def __str__(self):
        return self.username
