from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TasksForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def insert_tasks(request):
    """allows user to add tasks"""
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  
            task.user = request.user        
            task.save()
            return redirect('tables:all_tasks')
    else:
        form = TasksForm()
    return render(request, "tables/add_tasks.html", {'form': form})

@login_required
def all_tasks(request):
    """display all tasks of user"""
    tasks = Task.objects.filter(user=request.user)  # get only this user's tasks
    return render(request, "tables/list_tasks.html", {'tasks': tasks})


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('tables:home')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('tables:home')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):

    logout(request)

    return redirect('tables:login')