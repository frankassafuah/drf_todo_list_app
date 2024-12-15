from django.urls import path
from todos.views import CreateTodoAPIView, TodoListApiView, ListCreateTodosAPIView, RetrieveUpdateDestroyTodoAPIView


urlpatterns = [
    path("", ListCreateTodosAPIView.as_view(), name="todos"),
    path("<int:id>", RetrieveUpdateDestroyTodoAPIView.as_view(), name="detail-todo"),
    path("list/", TodoListApiView.as_view(), name="list-todos"),
    path("create/", CreateTodoAPIView.as_view(), name="create-todo"),
]
