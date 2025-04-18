# Generated by Django 5.0.4 on 2024-12-02 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0071_payment_process_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onsitepayment',
            name='rent_reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rent_payments', to='transportation.rented_cars', verbose_name='rent payment'),
        ),
        migrations.AlterField(
            model_name='payment_process',
            name='shop_processed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shoppayments', to='transportation.shops', verbose_name='Shop Payments'),
        ),
        migrations.AlterField(
            model_name='payment_process_items',
            name='payment_root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transportation.payment_process', verbose_name='root'),
        ),
        migrations.AlterField(
            model_name='payment_process_items',
            name='rent_transactions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='transportation.rented_cars', verbose_name='renttransaction'),
        ),
    ]
