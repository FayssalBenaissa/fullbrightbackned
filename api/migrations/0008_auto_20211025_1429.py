# Generated by Django 3.1.7 on 2021-10-25 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0007_auto_20211025_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afficheur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_afficheur', models.CharField(max_length=30)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apc',
            fields=[
                ('nom_APC', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('nom_commune', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Panneau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('type1', 'type1'), ('type2', 'type2'), ('type3', 'type3')], max_length=20)),
                ('itineraire', models.CharField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('designation', models.CharField(max_length=40)),
                ('nombre_facette', models.IntegerField()),
                ('hauteur', models.FloatField()),
                ('largeur', models.FloatField()),
                ('elevation', models.FloatField()),
                ('mecanisme', models.CharField(choices=[('mec1', 'mec1'), ('mec2', 'mec2'), ('mec3', 'mec3')], max_length=20)),
                ('circulation', models.BooleanField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('afficheur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.afficheur')),
                ('apc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.apc')),
                ('commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.commune')),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('nom_wilaya', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('num_wilaya', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('langue', models.CharField(choices=[('fr', 'fr'), ('ar', 'ar'), ('fr + ar', 'fr + ar')], max_length=20)),
                ('marque', models.CharField(max_length=40)),
                ('produit', models.CharField(max_length=40)),
                ('annonceur', models.CharField(max_length=40)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('panneau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.panneau')),
            ],
        ),
        migrations.AddField(
            model_name='panneau',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.wilaya'),
        ),
        migrations.AddField(
            model_name='commune',
            name='Wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.wilaya'),
        ),
        migrations.AddField(
            model_name='apc',
            name='commune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.commune'),
        ),
    ]
