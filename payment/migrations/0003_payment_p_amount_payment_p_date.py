# Generated by Django 4.1.1 on 2022-10-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='p_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='p_date',
            field=models.DateTimeField(null=True),
        ),
    ]
