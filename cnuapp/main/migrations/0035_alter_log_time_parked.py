# Generated by Django 3.2.8 on 2021-11-16 21:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='time_parked',
            field=models.DateTimeField(default=django.utils.timezone.now, unique=True),
        ),
    ]
