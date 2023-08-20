from django import forms
from .models import CustomUser, Customer, Vendor

class CustomerSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class VendorSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('address', 'phone_number', 'profile_picture')
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('company_name', 'description', 'logo')
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'logo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
