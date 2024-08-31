from django.contrib.auth import login, authenticate, logout
from .forms import CustomLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin/')
                else:
                    return redirect('home')  # Redirect to a non-admin home page
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def homepage_view(request):
    # Check if the user is authenticated and is a superuser
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # Redirect to the admin page if the user is a superuser
            return redirect('/admin/')
        else:
            # Render the home page template for normal users
            return render(request, 'your_app/homepage.html')  # Replace with your actual homepage template
    else:
        # Redirect to the login page if the user is not authenticated
        return redirect('/your-custom-login-url/')  # Replace with your login URL