from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .serializers import AbstractUser, User
from .models import Email


class UserModelSerializer:
    pass


class UserModelViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = UserModelSerializer

