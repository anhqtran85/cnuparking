# Generated by Django 3.2.8 on 2021-11-16 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0031_delete_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time_parked', models.DateTimeField(default=django.utils.timezone.now)),
                ('currently_parked_here', models.BooleanField(default=True, null=True)),
                ('time_left', models.DateTimeField(null=True, unique=True)),
                ('parking_spot', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotA_log', to='main.parking_a')),
                ('parking_spotB', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotB_log', to='main.parking_b')),
                ('parking_spotC1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotC1_log', to='main.parking_c1')),
                ('parking_spotC2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotC2_log', to='main.parking_c2')),
                ('parking_spotD', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotD_log', to='main.parking_d')),
                ('parking_spotE1', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotE1_log', to='main.parking_e1')),
                ('parking_spotE2', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotE2_log', to='main.parking_e2')),
                ('parking_spotE3', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotE3_log', to='main.parking_e3')),
                ('parking_spotE4', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotE4_log', to='main.parking_e4')),
                ('parking_spotF', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotF_log', to='main.parking_f')),
                ('parking_spotG', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotG_log', to='main.parking_g')),
                ('parking_spotH', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotH_log', to='main.parking_h')),
                ('parking_spotI', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotI_log', to='main.parking_i')),
                ('parking_spotJ', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotJ_log', to='main.parking_j')),
                ('parking_spotK', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotK_log', to='main.parking_k')),
                ('parking_spotL', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotL_log', to='main.parking_l')),
                ('parking_spotM', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotM_log', to='main.parking_m')),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotA_log', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
