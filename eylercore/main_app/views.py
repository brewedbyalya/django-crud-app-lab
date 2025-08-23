from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Project, Task, Tag
from .forms import ProjectForm, TaskForm, TagForm

def home(request):
    return render(request, 'main_app/home.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_app:projects_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def projects_index(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'main_app/projects_index.html', {'projects': projects})

@login_required
def projects_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    return render(request, 'main_app/projects_detail.html', {'project': project})

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('main_app:projects_index')
    else:
        form = ProjectForm()
    return render(request, 'main_app/add_project.html', {'form': form})

@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('main_app:projects_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main_app/edit_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('main_app:projects_index')
    return render(request, 'main_app/delete_project.html', {'project': project})

@login_required
def tasks_index(request):
    tasks = Task.objects.filter(project__user=request.user)
    return render(request, 'main_app/tasks_index.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_app:tasks_index')
    else:
        form = TaskForm()
        form.fields['project'].queryset = Project.objects.filter(user=request.user)
    return render(request, 'main_app/add_task.html', {'form': form})