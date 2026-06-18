from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TasksForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.shortcuts import get_object_or_404
# Create your views here.


@login_required
def home(request):

    tasks = Task.objects.filter(
        user=request.user
    )

    return render(
        request,
        'home.html',
        {'tasks': tasks}
    )

@login_required
def insert_tasks(request):

    if request.method == 'POST':
        form = TasksForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect('all_tasks')

    else:
        form = TasksForm()

    return render(request, "tables/add_tasks.html", {'form': form})

@login_required
def all_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tables/list_tasks.html", {'tasks': tasks})


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):

    logout(request)

    return redirect('login')

@login_required
def delete_task(request, id):

    task = Task.objects.get(id=id)

    task.delete()

    return redirect('all_tasks')

@login_required
def toggle_task(request, pk):

    task = get_object_or_404(
        Task,
        id=pk,
        user=request.user
    )

    task.completed = not task.completed

    task.save()

    return redirect('home')