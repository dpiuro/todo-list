from django.contrib import admin
from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['content', 'is_done', 'created_at', 'deadline']
    list_filter = ['is_done', 'created_at', 'deadline']
    search_fields = ['content', 'tags__name']
    ordering = ['created_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']