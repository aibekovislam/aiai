# Generated by Django 3.1.7 on 2023-01-23 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20230121_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carouselPicture', models.ManyToManyField(related_name='colorsM', to='core.ColorK')),
                ('productsPicture', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.products')),
            ],
        ),
    ]
