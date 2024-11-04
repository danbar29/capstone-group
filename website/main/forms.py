from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction, Project




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
        fields = ['donor_name', 'amount', 'transaction_type', 'date']
        labels = {
            'donor_name': 'Donor name ',
            'amount': 'Amount ',
            'transaction_type': 'Transaction type ',
            'date': 'Date ',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    
   

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'start_date', 'end_date', 'goal_amount', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'goal_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
