from django.urls import path
from . import views

app_name = 'tables'

urlpatterns = [
    path('', views.home, name='home'),
    path('addtasks/', views.insert_tasks, name='add_tasks'),
    path('alltasks/', views.all_tasks, name='all_tasks'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('complete/<int:pk>/', views.toggle_task, name='toggle_task'),
]