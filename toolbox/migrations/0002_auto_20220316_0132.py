# Generated by Django 3.2.9 on 2022-03-16 01:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed')])),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='AirlineAddRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$')])),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Option',
        ),
    ]
