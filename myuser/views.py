from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomerSignUpForm, VendorSignUpForm, CustomerProfileForm, VendorProfileForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Display an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')  # Assuming a radio button or select field for user type
        if user_type == 'customer':
            user_form = CustomerSignUpForm(request.POST)
            profile_form = CustomerProfileForm(request.POST)
        elif user_type == 'vendor':
            user_form = VendorSignUpForm(request.POST)
            profile_form = VendorProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful signup and login
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

def vendor_signup(request):
    if request.method == 'POST':
        user_form = VendorSignUpForm(request.POST)
        profile_form = VendorProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.is_vendor = True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('myuser:login')  # Redirect to login page after sign-up
    else:
        user_form = VendorSignUpForm()
        profile_form = VendorProfileForm()
    return render(request, 'vendor_signup.html', {'user_form': user_form, 'profile_form': profile_form})

# Rest of the code for customer_signup and vendor_signup as provided before
