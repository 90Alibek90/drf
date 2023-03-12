from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField()

    def __str__(self):
        return self.name

class User(models.Model):
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    hint = models.PositiveIntegerField()



class Email(models.Model):
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    hint = models.PositiveIntegerField()


    def __str__(self):
        return  f'{self.last_name}-{self.first_name}'