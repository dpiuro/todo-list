from django.urls import path
from . import views


app_name = "tasks"

urlpatterns = [
    path('', views.home, name='home'),
    path("", views.TaskListView.as_view(), name="task-list"),
    path("task/create/", views.TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", views.toggle_task_status, name="task-toggle"),
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path("tag/create/", views.TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),

    path("tasks/", views.TaskListView.as_view(), name="task-list"),
]
