# Generated by Django 4.1.1 on 2022-10-23 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tour_guide',
            fields=[
                ('tg_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tg_gender', models.CharField(max_length=50)),
                ('tg_nationality', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
