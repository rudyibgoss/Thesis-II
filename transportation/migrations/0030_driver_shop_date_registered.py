# Generated by Django 5.0.4 on 2024-10-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0029_driver_shop_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_shop',
            name='date_registered',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
