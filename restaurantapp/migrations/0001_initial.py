# Generated by Django 3.2.9 on 2021-11-18 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('restaurant_name', models.CharField(help_text='Give a Restaurant Name', max_length=30)),
                ('restaurant_description', models.CharField(help_text='Give a Short Description of Restaurant', max_length=500)),
                ('restaurant_start_time', models.TimeField(blank=True, help_text='Restaurant Opening time')),
                ('restaurant_off_time', models.TimeField(blank=True, help_text='Restaurant Closing time')),
                ('is_open', models.BooleanField(default=False, help_text='Is Restaurant Open Currently')),
                ('meta_data', models.JSONField(default=dict, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('meta_data', models.JSONField(default=dict, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(help_text='Relation of Restaurant', null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurantapp.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('is_available', models.BooleanField(default=True, help_text='This item is available or not')),
                ('meta_data', models.JSONField(default=dict, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('menu', models.ForeignKey(help_text='Relation of Menu', null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurantapp.menu')),
            ],
        ),
    ]