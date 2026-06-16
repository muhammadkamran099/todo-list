from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addtasks/', views.insert_tasks , name='add_tasks'),
    path('alltasks/', views.all_tasks , name='all_tasks'),
]