from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Common fields for all users
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    # Add any other shared fields
    
    def __str__(self):
        return self.username

class VendorGroup(models.Model):
    name = models.CharField(max_length=80, unique=True)
    members = models.ManyToManyField(CustomUser, related_name='vendor_groups')

class VendorPermission(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(CustomUser, related_name='vendor_permissions')

class CustomerGroup(models.Model):
    name = models.CharField(max_length=80, unique=True)
    members = models.ManyToManyField(CustomUser, related_name='customer_groups')

class CustomerPermission(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(CustomUser, related_name='customer_permissions')
