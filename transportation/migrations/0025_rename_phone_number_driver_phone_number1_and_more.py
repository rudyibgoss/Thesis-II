# Generated by Django 5.0.4 on 2024-10-15 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0024_alter_vehicle_categories_alter_vehicle_seat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='phone_number',
            new_name='phone_number1',
        ),
        migrations.AddField(
            model_name='driver',
            name='phone_number2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='phone_number3',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
