# Generated by Django 4.1.1 on 2022-10-23 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tourist', '0001_initial'),
        ('tour_guide', '0001_initial'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='t_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist.tourist'),
        ),
        migrations.AddField(
            model_name='payment',
            name='tg_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_guide.tour_guide'),
        ),
    ]
