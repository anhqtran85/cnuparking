# Generated by Django 3.2.8 on 2021-10-27 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_parking_a_parking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking_a',
            name='parking_status',
            field=models.BooleanField(null=True, verbose_name='Parking status'),
        ),
    ]