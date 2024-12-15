from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from todos.models import Todo
from rest_framework import response

# Create your views here.


class CreateTodoAPIView(CreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    # tell CreateAPIView to save the owner to the login user when creating this todo

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class TodoListApiView(ListAPIView):

    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user).all()



# Shortcut to List and Create Todos. Does the samething as the above views
class ListCreateTodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user).all()