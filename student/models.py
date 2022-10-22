from django.db import models


# Create your models here.

class Student(models.Model):
    s_id = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=50)
    s_sec = models.CharField(max_length=2)
    s_dep = models.CharField(max_length=4)
    about = models.TextField()


class VCaward(models.Model):
    session = models.CharField(max_length=10)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
