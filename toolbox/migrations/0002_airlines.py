# Generated by Django 3.2.9 on 2021-12-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
    ]