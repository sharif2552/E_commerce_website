from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomerSignUpForm, VendorSignUpForm, CustomerProfileForm, VendorProfileForm
from myuser.backends import EmailBackend
from django.contrib.auth import logout


from django.contrib.auth import get_user_model
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        
        print(user)
        if user is not None:
            print("valid user")
            login(request, user)
            return redirect('products:homepage')  # Redirect to the home page after successful login
        else:
            print('login failed')
            # Display an error message
            error_message = 'Invalid email or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        user_type = 'customer'  # Assuming a radio button or select field for user type
        if user_type == 'customer':
            user_form = CustomerSignUpForm(request.POST)
            
            profile_form = CustomerProfileForm(request.POST, request.FILES)

        elif user_type == 'vendor':
            user_form = VendorSignUpForm(request.POST)
            profile_form = VendorProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            print(profile_form.cleaned_data)
            print(profile_form.cleaned_data['profile_picture'])
                # Create a user instance but do not save it yet 
            user = user_form.save(commit=False)
                
                # Set and hash the user's password
            password = user_form.cleaned_data['password']
            user.set_password(password)
                
                # Now save the user instance
            user.save()
                
                # Create a customer profile instance and associate it with the user
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user, backend='myuser.backends.EmailBackend')
            return redirect('products:homepage')  # Redirect to the home page after successful signup and login
    else:
        user_form = CustomerSignUpForm()
        profile_form = CustomerProfileForm()
    
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})


def customer_signup(request):
    if request.method == 'POST':
        user_form = CustomerSignUpForm(request.POST)
        profile_form = CustomerProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_customer = True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('myuser:login')  # Redirect to login page after sign-up
    else:
        user_form = CustomerSignUpForm()
        profile_form = CustomerProfileForm()
    return render(request, 'customer_signup.html', {'user_form': user_form, 'profile_form': profile_form})

def vendor_signup_view(request):
    if request.method == 'POST':
        user_form = VendorSignUpForm(request.POST)
        profile_form = VendorProfileForm(request.POST, request.FILES)
        email_exists = False
        if user_form.is_valid() and profile_form.is_valid():
            email = user_form.cleaned_data['email']
            
            # Check if the email already exists
            if get_user_model().objects.filter(email=email).exists():
                email_exists = True 
            else:
                user = user_form.save(commit=False)
                user.is_vendor = True
                password = user_form.cleaned_data['password']
                user.set_password(password)
                user.save()
                
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                
                return redirect('myuser:vendor_login')  # Redirect to login page after sign-up
    else:
        email_exists = False
        user_form = VendorSignUpForm()
        profile_form = VendorProfileForm()
        
    return render(request, 'vendor_signup.html', {'user_form': user_form, 'profile_form': profile_form, 'email_exists': email_exists})


# Rest of the code for customer_signup and vendor_signup as provided before

def vendor_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password,  )
        
        print(user)
        if user is not None:
            print("valid user")
            login(request, user)
            return redirect('vendors:vendor_dashboard')  # Redirect to the home page after successful login
        else:
            print('login failed')
            # Display an error message
            error_message = 'Invalid email or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'vendor_login.html')


def logout_view(request):
    logout(request)
    return redirect('myuser:login')



# myapp/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def my_account(request):
    user = request.user
    if user.is_customer:
        profile = user.customer_profile
        user_type = 'Customer'
    elif user.is_vendor:
        profile = user.vendor_profile
        user_type = 'Vendor'
    else:
        profile = None
        user_type = 'Regular User'

    context = {
        'user_type': user_type,
        'profile': profile,
    }
    return render(request, 'my_account.html', context)
