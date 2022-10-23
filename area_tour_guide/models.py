from django.db import models
from tour_guide.models import tour_guide


class area_tour_guide(models.Model):
    atg_id = models.IntegerField(primary_key=True)
    area_name = models.CharField(max_length=50)
    tg_id = models.ForeignKey(tour_guide, on_delete=models.CASCADE)
