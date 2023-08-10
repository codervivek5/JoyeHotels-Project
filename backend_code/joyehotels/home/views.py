from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html', {'user_authenticated': request.user.is_authenticated, 'user': request.user})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("Username:", username)
        print("Password:", password)
        
        user = authenticate(request, username=username, password=password)

        print("User:", user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'login.html', {'error_message': messages.get_messages(request)})

# @login_required(login_url='home')  # Redirects authenticated users to the 'home' page
def register_view(request):
    
    if request.user.is_authenticated:
        return redirect('home')


    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.warning(request, "Passwords do not match!")
            return redirect('/register')  # Redirect back to the registration page with the error message

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            messages.warning(request, "Username already exists!")
            return redirect('/register')  # Redirect back to the registration page with the error message

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('/login')  # Redirect to the login page after successful registration

    return render(request, 'register.html')  # Show the registration form for non-authenticated users




def logout_view(request):
    logout(request)
    return redirect('home')

def hotels(request):
    return render(request, 'hotels.html')
