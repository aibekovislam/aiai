# Generated by Django 3.1.7 on 2023-01-19 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='p',
        ),
    ]
