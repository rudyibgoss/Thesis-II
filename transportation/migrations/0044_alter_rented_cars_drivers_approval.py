# Generated by Django 5.0.4 on 2024-11-18 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0043_rented_cars_drivers_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rented_cars',
            name='drivers_approval',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
