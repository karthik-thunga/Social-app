from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib import messages

# Creating dashboard view

@login_required
def dashboard(request):
    return render(
        request, 'accounts/dashboard.html', { 'section':'dashboard' }
    )

# User registration 

def user_registration(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'User created successfully')
            return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/user_registration.html', {'form':form})

