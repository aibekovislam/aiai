# Generated by Django 4.1.5 on 2023-01-31 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_colork_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paymentMethod',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
