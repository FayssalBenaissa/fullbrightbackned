# Generated by Django 3.1.7 on 2021-11-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20211116_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afficheur',
            name='nom_afficheur',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]