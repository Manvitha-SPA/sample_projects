# Generated by Django 4.2.4 on 2023-10-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_alter_restaurant_r_apc_alter_restaurant_r_timings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='R_cu',
            field=models.CharField(default=['a', 'b', 'c'], max_length=500),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='R_pay',
            field=models.CharField(default='Cash or Cards Accepted', max_length=500),
        ),
    ]