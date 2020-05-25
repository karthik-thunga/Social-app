from django.shortcuts import render, redirect
from .forms import ImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def image_create(request):

    if request.method == 'POST':
        form = ImageForm(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            new_form = form.save(commit=False)

            new_form.user = request.user
            new_form.save()
            messages.success(request, "Image added successfully")
            return redirect(new_form.get_absolute_url())
    else:
        form = ImageForm(data=request.GET)

    return render(request, 'images/create.html', { 'form' : form, 'section' : 'images' })

