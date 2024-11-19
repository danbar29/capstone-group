from django.shortcuts import render, redirect
from .forms import RegisterForm, TransactionForm, ProjectForm
from .models import Transaction, Project
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
#from django.contrib.auth.decorators import login_required #if we want to go with decorators we could add @login_required

# Create your views here.
def log_out(request):
    logout(request)
    return redirect("/login/")

def donations(request):
    return render(request, 'main/donations.html')

def trends(request):
    transactions = Transaction.objects.filter(fund="general")
    return render(request, 'main/trends.html', {'transactions': transactions})


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
    
    # Only show non-archived projects
    projects = Project.objects.filter(is_archived=False) #projects = Project.objects.all()
    
    # Prepare projects with their total donations and calculate progress
    project_data = []
    for project in projects:
        total_raised = project.transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        progress_percentage = (total_raised / project.goal_amount) * 100 if project.goal_amount > 0 else 0
        project_data.append({
            'project': project,
            'total_raised': total_raised,
            'progress_percentage': round(progress_percentage, 2),
            'is_owner': project.owner ==request.user

        })
    
    return render(request, 'main/home.html', {
        'general_total': general_total,
        'project_data': project_data
    })



def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)  # Not saving yet to fetch the user.
            project.owner = request.user
            project.save()  # push it to the database with the associated user.
            messages.success(request, 'Project created successfully.')
            return redirect('create_project')  # Redirect to refresh the page and clear fields.
    else:
        form = ProjectForm()
    return render(request, 'main/create_project.html', {'form': form})



def add_general_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.fund = 'general'
            if transaction.transaction_type == 'Debit':
                transaction.amount = -transaction.amount  # If the transaction is debit, make the amount negative.
            transaction.save()
            messages.success(request, 'General transaction added successfully.')
            return redirect('add_general_transaction')  # Redirect to refresh the page and clear fields.
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
            if transaction.transaction_type == 'Debit':
                transaction.amount = -transaction.amount  # If the transaction is debit, make the amount negative.
            transaction.save()
            messages.success(request, f'Transaction added successfully to {project.name}.')
            return redirect('add_project_transaction', project_id=project.id)  # Redirect to refresh the page and clear fields.
    else:
        form = TransactionForm()
    return render(request, 'main/add_project_transaction.html', {'form': form, 'project': project})



def view_project_transactions(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    transactions = project.transactions.all()
    total_raised = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'main/view_project_transactions.html', {
        'project': project,
        'transactions': transactions,
        'total_raised': total_raised
    })


def view_general_transactions(request):
    transactions = Transaction.objects.filter(fund="general")
    return render(request, 'main/view_general_transactions.html', {'transactions': transactions})


def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully.')
            return redirect('home')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/edit_project.html', {'form': form, 'project': project})

def archive_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if project.owner == request.user:
        project.is_archived = True
        project.save()
        return redirect('home')  # Redirect to the homepage after archiving
    else:
        return redirect('home')  # Redirect if the user does not own the project
    

def archived_projects(request):
    # Retrieve all archived projects
    archived_projects_list = Project.objects.filter(is_archived=True)

    # Prepare project data with the total raised amount and progress percentage
    project_data = []
    for project in archived_projects_list:
        total_raised = project.transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        progress_percentage = (total_raised / project.goal_amount * 100) if project.goal_amount > 0 else 0
        project_data.append({
            'project': project,
            'total_raised': total_raised,
            'progress_percentage': progress_percentage
        })

    return render(request, 'main/archived_projects.html', {'archived_projects': project_data})

# Function to restore an archived project
def restore_project(request, project_id):
    project = Project.objects.get(id=project_id)
    if project and project.is_archived:
        project.is_archived = False
        project.save()
        return redirect('home')  # Redirect back to home page after restoring
