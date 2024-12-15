from django.urls import path
from todos.views import CreateTodoAPIView, TodoListApiView


urlpatterns = [
    path("list/", TodoListApiView.as_view(), name="todos"),
    path("create/", CreateTodoAPIView.as_view(), name="create-todo"),
]
