# Generated by Django 3.1.7 on 2023-01-23 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_products_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='picture',
        ),
        migrations.AddField(
            model_name='products',
            name='colors',
            field=models.ManyToManyField(related_name='colors', to='core.ColorK'),
        ),
        migrations.DeleteModel(
            name='CarouselM',
        ),
    ]
