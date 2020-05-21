from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.get(email=email):
            raise forms.ValidationError('Email Already Exist')

        return email


