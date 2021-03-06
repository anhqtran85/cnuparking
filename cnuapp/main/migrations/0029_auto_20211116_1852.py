# Generated by Django 3.2.8 on 2021-11-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_log_time_parked'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='log',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='log',
            constraint=models.UniqueConstraint(fields=('username', 'time_parked'), name='unique log'),
        ),
        migrations.AlterModelTable(
            name='log',
            table='log',
        ),
    ]
