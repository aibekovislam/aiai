# Generated by Django 4.1.5 on 2023-01-31 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_order_paymentmethod_order_bankcartmethod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='bankCartMethod',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Банковская карта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cashMethod',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Наличным способом'),
        ),
        migrations.AlterField(
            model_name='order',
            name='mbank',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='МБанк'),
        ),
    ]