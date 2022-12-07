from django.db import models
from tourist_spot.models import tourist_spot

class emergency(models.Model):
    em_id = models.IntegerField(primary_key=True)
    station_name = models.CharField(max_length=50)
    contact = models.IntegerField(null=True)
    ts_id = models.ForeignKey(tourist_spot, on_delete=models.CASCADE)