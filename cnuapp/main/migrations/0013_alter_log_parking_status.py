# Generated by Django 3.2.8 on 2021-11-11 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211111_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='parking_status',
            field=models.BooleanField(null=True),
        ),
    ]