# Generated by Django 5.0.4 on 2024-12-01 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0067_rented_cars_liquidated_rented_cars_share_rates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rented_cars',
            name='share_rates',
            field=models.IntegerField(default=0),
        ),
    ]
