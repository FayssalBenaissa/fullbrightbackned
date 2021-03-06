# Generated by Django 3.1.7 on 2021-12-09 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20211205_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pub',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pub',
            name='annonceur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.annonceur'),
        ),
        migrations.AlterField(
            model_name='pub',
            name='marque',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.marque'),
        ),
        migrations.AlterField(
            model_name='pub',
            name='produit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.produit'),
        ),
    ]
