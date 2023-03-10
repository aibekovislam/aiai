# Generated by Django 3.1.7 on 2023-01-21 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_colork_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='colors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.colork'),
        ),
        migrations.AlterField(
            model_name='colork',
            name='picture',
            field=models.ImageField(blank=True, db_index=True, upload_to='product__image', verbose_name='Картинка цветов'),
        ),
    ]
