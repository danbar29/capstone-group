from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction


# add email form, can add more fields for user
class RegisterForm(UserCreationForm):
    # add custom fields to registration page
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    usable_password = None
    class Meta:
        model = User
        fields = ["username", "email","first_name","last_name","password1","password2"]
        
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['fund', 'amount', 'date', 'transaction_type', 'description']
        widgets = {
            'fund': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the amount'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'transaction_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter a brief description'}),
        }
        
        help_texts = {
            'amount': 'Enter the transaction amount in USD.',
            'date': 'Select the date for this transaction.',
        }


