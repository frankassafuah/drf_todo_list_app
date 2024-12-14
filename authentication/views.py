from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status
from django.contrib.auth import authenticate

# Create your views here.


class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data) # Pass user input data and deserialize

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        user = authenticate(
            username=email, password=password
        )  # returns none if authentication fails

        if user is not None:
            serializer = self.serializer_class(user) # Serialize the user instance
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response({"message": "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)