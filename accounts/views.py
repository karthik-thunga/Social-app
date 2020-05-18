from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Creating dashboard view

@login_required
def dashboard(request):
    return render(
        request, 'accounts/dashboard.html', { 'section':'dashboard' }
    )