from django.urls import path
from . import views

urlpatterns = [
    path("task/", views.TaskView.as_view()),
    path("task/list/todo/", views.TaskToDoView.as_view()),
    path("task/<int:task_id>/", views.TaskDetailView.as_view()),
]
