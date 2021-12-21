# Generated by Django 3.1.7 on 2021-11-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20211027_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonnement',
            name='date_debut',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='abonnement',
            name='date_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_creation',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_debut',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='edition',
            name='date',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='pub',
            name='date_creation',
            field=models.DateField(auto_now_add=True),
        ),
    ]
