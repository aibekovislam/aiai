# Generated by Django 4.1.5 on 2023-02-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='colorsCountValue',
            field=models.CharField(max_length=255, null=True, verbose_name='Количество расцветок'),
        ),
        migrations.AddField(
            model_name='order',
            name='colorsValue',
            field=models.CharField(max_length=255, null=True, verbose_name='Расцветки'),
        ),
    ]
