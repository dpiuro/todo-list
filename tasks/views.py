from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "tasks/task_list.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().order_by("is_done", "-created_at")
        return queryset


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ["content", "deadline", "tags", "is_done"]
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "tasks/tag_list.html"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("tasks:task-list")

def home(request):
    total_tasks = Task.objects.count()
    total_tags = Tag.objects.count()
    context = {
        "total_tasks": total_tasks,
        "total_tags": total_tags,
    }
    return render(request, "tasks/home.html", context)
