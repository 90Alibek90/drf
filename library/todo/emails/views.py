from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework import viewsets, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

# Create your views here.
from .serializers import AbstractUser, User
from .models import Email


class ExampleView(APIView):
    permission_classes = [AllowAny]

class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff

class UserModelSerializer:
    pass


class UserModelViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = UserModelSerializer

