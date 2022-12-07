from django.db import models
from user.models import User


# Create your models here.
class tourist(models.Model):
    t_id = models.IntegerField(primary_key=True)
    t_date_of_birth = models.DateField(null=True)
    t_gender = models.CharField(max_length=50)
    t_nationality = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
