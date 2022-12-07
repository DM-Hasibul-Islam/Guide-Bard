from django.db import models
from tourist.models import tourist
from tour_guide.models import tour_guide

class booking(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    t_id = models.ForeignKey(tourist, on_delete=models.CASCADE)
    tg_id = models.ForeignKey(tour_guide, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    amount = models.IntegerField(null=True)
