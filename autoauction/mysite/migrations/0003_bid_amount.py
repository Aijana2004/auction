# Generated by Django 5.1.7 on 2025-03-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_car_brand_en_car_brand_ky_car_brand_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='amount',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
