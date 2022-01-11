# Generated by Django 3.2.8 on 2021-11-16 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_parking_b_parking_c1_parking_c2_parking_d_parking_e1_parking_e2_parking_e3_parking_e4_parking_f_park'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='parking_spotB',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotB_log', to='main.parking_b'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotC1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotC1_log', to='main.parking_c1'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotC2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotC2_log', to='main.parking_c2'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotD',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotD_log', to='main.parking_d'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotE1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotE1_log', to='main.parking_e1'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotE2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotE2_log', to='main.parking_e2'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotE3',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotE3_log', to='main.parking_e3'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotE4',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotE4_log', to='main.parking_e4'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotF',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotF_log', to='main.parking_f'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotG',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotG_log', to='main.parking_g'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotH',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotH_log', to='main.parking_h'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotI',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotI_log', to='main.parking_i'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotJ',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotJ_log', to='main.parking_j'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotL',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotL_log', to='main.parking_l'),
        ),
        migrations.AddField(
            model_name='log',
            name='parking_spotM',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking_spotM_log', to='main.parking_m'),
        ),
    ]
