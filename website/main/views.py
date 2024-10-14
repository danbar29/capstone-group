from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login,logout, authenticate


# Create your views here.
def log_out(request):
    logout(request)
    return redirect("/login/")

def home(request):
    return render(request, 'main/home.html')

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

