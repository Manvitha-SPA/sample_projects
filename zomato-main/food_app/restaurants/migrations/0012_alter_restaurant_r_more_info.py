# Generated by Django 4.2.4 on 2023-10-05 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_restaurant_r_reserve_restaurant_r_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='R_more_info',
            field=models.CharField(default=['ac', 'bd'], max_length=500),
        ),
    ]
