# Generated by Django 3.2.7 on 2021-09-26 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studentId',
            new_name='studentid',
        ),
    ]
