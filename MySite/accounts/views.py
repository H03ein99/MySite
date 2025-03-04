from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return redirect('/')
                
            else:
                messages.error(request, "Username or Password incorrect")
                form = AuthenticationForm()
                return render(request, 'accounts/login.html', {'form': form})
        else:
            form = AuthenticationForm()
            context = {'form': form}
            return render(request, 'accounts/login.html', context)
    else:
        messages.error(request, "Already logged in")
        return redirect('/')

@login_required        
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/')
    

def signup_view(request):
    if request.user.is_authenticated:
        messages.error(request, 'Already logged in')
        return redirect('/')
    else:    
        if request.method == 'GET':
            form = CustomUserCreationForm()
            context = {'form': form}
            return render(request, 'accounts/signup.html', context)
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User Created Successfully')
                return redirect('/')
            else:
                messages.error(request, 'Try Again')    
                form = CustomUserCreationForm()
                context = {'form': form}
                return render(request, 'accounts/signup.html', context)    