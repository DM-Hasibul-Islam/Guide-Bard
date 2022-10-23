from django.db import models
from user.models import User
# Create your models here.
class tour_guide(models.Model):
    tg_id = models.IntegerField(primary_key=True)
    tg_date_of_birth = models.DateField
    tg_gender = models.CharField(max_length=50)
    tg_nationality = models.CharField(max_length=50)
    tg_rating = models.FloatField
    user = models.ForeignKey(User, on_delete=models.CASCADE)