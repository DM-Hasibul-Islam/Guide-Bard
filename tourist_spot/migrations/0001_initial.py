# Generated by Django 4.1.1 on 2022-10-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tourist_spot',
            fields=[
                ('ts_id', models.IntegerField(primary_key=True, serialize=False)),
                ('spot_name', models.CharField(max_length=100)),
            ],
        ),
    ]
