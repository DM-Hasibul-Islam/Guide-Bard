from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    U_id = models.IntegerField(primary_key=True)
    U_first_name = models.CharField(max_length=50)
    U_last_name = models.CharField(max_length=50)
    U_email = models.CharField(max_length=50)
    U_name = models.CharField(max_length=50)
    U_pass = models.CharField(max_length=50)
