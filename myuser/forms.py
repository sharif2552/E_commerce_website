from django import forms
from .models import Customer, Vendor
from django.contrib.auth import get_user_model

class CustomerSignUpForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')  # Add other fields as needed

class VendorSignUpForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')  # Add other fields as needed

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('address', 'phone_number', 'profile_picture')  # Add other fields as needed

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('company_name', 'description', 'logo')  # Add other fields as needed
