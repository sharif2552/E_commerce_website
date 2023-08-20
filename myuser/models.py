from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you need
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='customer_profiles/', blank=True, null=True)
    # Add any other customer-specific fields

class Vendor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor_profile')
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='vendor_logos/', blank=True, null=True)
    # Add any other vendor-specific fields
