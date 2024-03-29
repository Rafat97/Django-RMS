# Generated by Django 3.2.9 on 2021-11-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='meta_data',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='meta_data',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='meta_data',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
