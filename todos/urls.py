from django.urls import path
from todos.views import CreateTodoAPIView, TodoListApiView, ListCreateTodosAPIView


urlpatterns = [
    path("", ListCreateTodosAPIView.as_view(), name="todos"),
    path("list/", TodoListApiView.as_view(), name="list-todos"),
    path("create/", CreateTodoAPIView.as_view(), name="create-todo"),
]
