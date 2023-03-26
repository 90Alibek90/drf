from django.db import models

# Create your models here.

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

class Author(models.Model):
    name = models.CharField(max_length=64, unique=True)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name