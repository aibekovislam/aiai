# Generated by Django 4.1.5 on 2023-01-25 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_codep_customer_phone_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='username',
        ),
    ]
