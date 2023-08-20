"""
Views for the user API.
"""
from rest_framework import generics
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serilizer_class = UserSerializer