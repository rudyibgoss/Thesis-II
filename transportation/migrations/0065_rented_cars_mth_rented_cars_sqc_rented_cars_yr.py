# Generated by Django 5.0.4 on 2024-11-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0064_alter_rented_cars_execes_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rented_cars',
            name='mth',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rented_cars',
            name='sqc',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rented_cars',
            name='yr',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
