# Generated by Django 3.1.7 on 2021-10-21 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211021_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apc',
            name='commune',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.commune'),
        ),
        migrations.AlterField(
            model_name='panneau',
            name='apc',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='api.apc'),
        ),
    ]
