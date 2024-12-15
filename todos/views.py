from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from todos.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from todos.models import Todo
from rest_framework import response
from django_filters.rest_framework import DjangoFilterBackend
from todos.pagination import CustomPageNumberPagination

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


# ------------------------


# Shortcut to List and Create Todos. Does the same thing as the above views
class ListCreateTodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["title", "description"]
    search_fields = ["title", "description"]  # e.g url?search=name
    ordering_fields = ["id", "title", "description"] #e.g url?ordering=id
    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user).all()


class RetrieveUpdateDestroyTodoAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user).all()
