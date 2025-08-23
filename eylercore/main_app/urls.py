from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    
    # Project
    path('projects/', views.projects_index, name='projects_index'),
    path('projects/<int:project_id>/', views.projects_detail, name='project_detail'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    
    # Tag
    path('tags/', views.tags_index, name='tags_index'),
    path('tags/add/', views.add_tag, name='add_tag'),
    path('tags/<int:tag_id>/edit/', views.edit_tag, name='edit_tag'),
    path('tags/<int:tag_id>/delete/', views.delete_tag, name='delete_tag'),
    
    # Task
    path('projects/<int:project_id>/tasks/', views.tasks_index, name='tasks_index'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('projects/<int:project_id>/tasks/add/', views.add_task, name='add_task'),
    path('projects/<int:project_id>/tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('projects/<int:project_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]
