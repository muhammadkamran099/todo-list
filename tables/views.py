from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TasksForm
# Create your views here.

def home(request):
    return HttpResponse("Welcome to Todo Application")

#@login_required
def insert_tasks(request):
    """allows user to add tasks"""
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # don't save yet
            task.user = request.user        # link user
            task.save()
            return redirect('home')
    else:
        form = TasksForm()
    return render(request, "tables/add_tasks.html", {'form': form})

#@login_required
def all_tasks(request):
    """display all tasks of user"""
    tasks = Task.objects.filter(user=request.user)  # get only this user's tasks
    return render(request, "tables/list_tasks.html", {'tasks': tasks})
    
    

