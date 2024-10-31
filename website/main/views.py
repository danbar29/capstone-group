from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login,logout, authenticate
from .forms import TransactionForm
from django.contrib import messages



# Create your views here.
def log_out(request):
    logout(request)
    return redirect("/login/")

def home(request):
    return render(request, 'main/home.html')

def donations(request):
    return render(request, 'main/donations.html')

def trends(request):
    return render(request, 'main/trends.html')


def sign_up(request):
    if request.method == 'POST':
        # populate form whatever data was
        form = RegisterForm(request.POST)
        
        # if method is on form, validate it is correct
        if form.is_valid():
            user = form.save()
            # login user
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form} )


def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            messages.success(request, 'Transaction added successfully.')
            form = TransactionForm()  # Clear the form after successful submission
            return redirect('add_transaction')  # Redirect to show the success message and reset the form
        else:
            messages.error(request, 'There was an error with your submission. Please check the fields.')

    else:
        form = TransactionForm()

    return render(request, 'main/add_transaction.html', {'form': form})

def transaction_success(request):
    return render(request, 'main/transaction_success.html')
