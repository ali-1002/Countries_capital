# Generated by Django 5.2.1 on 2025-06-03 22:27

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapitalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CountriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
                ('country_population', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2000000000)])),
                ('capital_population', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100000000)])),
                ('country_flag_photos', models.ImageField(blank=True, default='default_flag/img.png', upload_to='flag_photos')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('capital_name', models.OneToOneField(default='.', on_delete=django.db.models.deletion.CASCADE, to='countries.capitalmodel')),
            ],
            options={
                'db_table': 'countries',
            },
        ),
    ]
