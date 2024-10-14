from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# add email form, can add more fields for user
class RegisterForm(UserCreationForm):
    # add custom fields to registration page
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email","first_name","last_name","password1","password2"]