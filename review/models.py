from django.db import models
from tourist.models import tourist
from tour_guide.models import tour_guide


class review(models.Model):
    r_id = models.IntegerField(primary_key=True)
    tg_id = models.ForeignKey(tour_guide, on_delete=models.CASCADE)
    t_id = models.ForeignKey(tourist, on_delete=models.CASCADE)
    review = models.TextField
    star = models.FloatField