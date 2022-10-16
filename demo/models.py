from django.db import models

from django.contrib.auth import base_user


# Create your models here.

class login(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class signup(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirmPassword = models.CharField(max_length=30)
