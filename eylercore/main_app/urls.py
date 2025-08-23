from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_index, name='projects_index'),
    path('projects/<int:project_id>/', views.projects_detail, name='project_detail'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('tasks/', views.tasks_index, name='tasks_index'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('signup/', views.signup, name='signup'),
]