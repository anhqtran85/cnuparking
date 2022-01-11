# Generated by Django 3.2.7 on 2021-11-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_parking_a_parking_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parking_K',
            fields=[
                ('parking_spot', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Parkingk spot')),
                ('parking_status', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='parking_a',
            name='parking_status',
            field=models.BooleanField(null=True),
        ),
    ]