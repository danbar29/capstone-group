from .forms import RegisterForm
from django.contrib.auth import login,logout, authenticate
from .forms import TransactionForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.db.models import Sum
from .models import Transaction, Project
from .forms import TransactionForm, ProjectForm



# Create your views here.
def log_out(request):
    logout(request)
    return redirect("/login/")

#def home(request):
 #   return render(request, 'main/home.html')

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


def home(request):
    general_total = Transaction.objects.filter(fund="general").aggregate(Sum('amount'))['amount__sum'] or 0
    projects = Project.objects.all()
    
    # Prepare projects with their total donations
    project_data = []
    for project in projects:
        total_raised = project.transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        project_data.append({
            'project': project,
            'total_raised': total_raised
        })
    
    return render(request, 'main/home.html', {
        'general_total': general_total,
        'project_data': project_data
    })

def view_general_transactions(request):
    transactions = Transaction.objects.filter(fund="general")
    return render(request, 'main/view_general_transactions.html', {'transactions': transactions})



def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created successfully.')
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'main/create_project.html', {'form': form})

def view_project_transactions(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    transactions = project.transactions.all()
    total_raised = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'main/view_project_transactions.html', {
        'project': project,
        'transactions': transactions,
        'total_raised': total_raised
    })


def add_general_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.fund = 'general'
            transaction.save()
            messages.success(request, 'General transaction added successfully.')
            # After saving the form, create a new instance of the form to clear fields
            form = TransactionForm()  # This clears the form
    else:
        form = TransactionForm()

    return render(request, 'main/add_general_transaction.html', {'form': form})

def add_project_transaction(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.project = project
            transaction.fund = 'specific'
            transaction.save()
            messages.success(request, f'Transaction added successfully to {project.name}.')
            # Clear the form after saving by creating a new instance
            form = TransactionForm()  # Clears the form
    else:
        form = TransactionForm()

    return render(request, 'main/add_project_transaction.html', {'form': form, 'project': project})










