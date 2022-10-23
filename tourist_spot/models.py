from django.db import models

# Create your models here.
class tourist_spot(models.Model):
    ts_id = models.IntegerField(primary_key=True)
    spot_name = models.CharField(max_length=100)
    spot_details = models.TextField
