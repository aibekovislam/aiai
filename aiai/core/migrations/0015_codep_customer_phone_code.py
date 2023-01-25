# Generated by Django 4.1.5 on 2023-01-25 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_colork_picture_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=7, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.codep'),
        ),
    ]
