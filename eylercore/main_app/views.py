from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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

# Project Views
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
            return redirect('main_app/projects_index.html')
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
            return redirect('main_app/projects_detail.html', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main_app/edit_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('main_app/projects_index')
    return render(request, 'main_app/delete_project.html', {'project': project})

# Tag Views
@login_required
def tags_index(request):
    tags = Tag.objects.all()
    return render(request, 'tags/index.html', {'tags': tags})

@login_required
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tags_index')
    else:
        form = TagForm()
    return render(request, 'tags/form.html', {'form': form, 'action': 'Add'})

@login_required
def edit_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tags_index')
    else:
        form = TagForm(instance=tag)
    return render(request, 'tags/form.html', {'form': form, 'action': 'Edit', 'tag': tag})

@login_required
def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == 'POST':
        tag.delete()
        return redirect('tags_index')
    return render(request, 'tags/delete.html', {'tag': tag})

@login_required
def tasks_index(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    tasks = project.tasks.all()
    return render(request, 'tasks/index.html', {'project': project, 'tasks': tasks})

@login_required
def task_detail(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    task = get_object_or_404(Task, id=task_id, project=project)
    return render(request, 'tasks/detail.html', {'project': project, 'task': task})

@login_required
def add_task(request, project_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, project=project)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            form.save_m2m() 
            return redirect('tasks_index', project_id=project.id)
    else:
        form = TaskForm(project=project)
    return render(request, 'tasks/form.html', {
        'project': project, 
        'form': form, 
        'action': 'Add'
    })

@login_required
def edit_task(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    task = get_object_or_404(Task, id=task_id, project=project)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, project=project)
        if form.is_valid():
            form.save()
            return redirect('task_detail', project_id=project.id, task_id=task.id)
    else:
        form = TaskForm(instance=task, project=project)
    return render(request, 'tasks/form.html', {
        'project': project, 
        'form': form, 
        'action': 'Edit', 
        'task': task
    })

@login_required
def delete_task(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id, user=request.user)
    task = get_object_or_404(Task, id=task_id, project=project)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks_index', project_id=project.id)
    return render(request, 'tasks/delete.html', {
        'project': project, 
        'task': task
    })