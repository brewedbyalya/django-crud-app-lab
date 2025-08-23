from django.contrib import admin
from .models import Project, Task, Tag

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['name', 'description']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'priority', 'due_date']
    list_filter = ['status', 'priority', 'created_at']
    search_fields = ['title', 'description']
    filter_horizontal = ['tags']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['name']