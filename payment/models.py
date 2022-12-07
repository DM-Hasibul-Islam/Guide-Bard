from django.db import models
from tourist.models import tourist
from tour_guide.models import tour_guide
from booking.models import booking


class payment(models.Model):
    p_id = models.IntegerField(primary_key=True)
    method = models.CharField(max_length=50)
    trx_Id = models.CharField(max_length=50)
    booking_id = models.ForeignKey(booking, on_delete=models.CASCADE)
    tg_id = models.ForeignKey(tour_guide, on_delete=models.CASCADE)
    t_id = models.ForeignKey(tourist, on_delete=models.CASCADE)
    p_amount = models.IntegerField(null=True)
    p_date = models.DateTimeField(null=True)
