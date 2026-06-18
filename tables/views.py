from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import Task


# ---------------- HOME ----------------
@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})


# ---------------- ADD TASK ----------------
@login_required
def insert_tasks(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')

        Task.objects.create(
            user=request.user,
            title=title,
            priority=priority,
            due_date=due_date if due_date else None
        )

        return redirect('home')

    return render(request, "tables/add_tasks.html")


# ---------------- ALL TASKS ----------------
@login_required
def all_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tables/list_tasks.html", {'tasks': tasks})


# ---------------- REGISTER ----------------
def register_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'register.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(request, user)
        return redirect('home')

    return render(request, 'register.html')


# ---------------- LOGIN ----------------
def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {
            'form': form,
            'error': 'Invalid credentials'
        })

    return render(request, 'login.html')


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login')


# ---------------- DELETE TASK ----------------
@login_required
def delete_task(request, id):

    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()

    return redirect('home')


# ---------------- TOGGLE TASK ----------------
@login_required
def toggle_task(request, pk):

    task = get_object_or_404(Task, id=pk, user=request.user)

    task.completed = not task.completed
    task.save()

    return redirect('home')