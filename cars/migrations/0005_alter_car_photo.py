# Generated by Django 4.1 on 2025-01-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cars', '0004_alter_car_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
    ]
