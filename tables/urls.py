from django.urls import path
from . import views
from .views import (
    home,
    register_view,
    login_view,
    logout_view
)

app_name = 'tables'

urlpatterns = [
    path('', home, name='home'),
    path('addtasks/', views.insert_tasks , name='add_tasks'),
    path('alltasks/', views.all_tasks , name='all_tasks'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]