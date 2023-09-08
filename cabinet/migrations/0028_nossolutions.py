# Generated by Django 4.2 on 2023-05-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0027_alter_apropos_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='NosSolutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='NosSolutions', max_length=255, null=True)),
                ('titrepage', models.TextField(blank=True, null=True, verbose_name='Titre de la page')),
                ('titreD', models.TextField(blank=True, null=True, verbose_name='Titre programme Diamond')),
                ('soustitreD', models.TextField(blank=True, null=True, verbose_name='Sous-titre programme Diamond')),
                ('imageD', models.ImageField(blank=True, null=True, upload_to='nossolutions/')),
                ('descriptionD', models.TextField(blank=True, null=True, verbose_name='Description programme Diamond')),
                ('voirplusD', models.CharField(blank=True, max_length=255, null=True)),
                ('titreF', models.TextField(blank=True, null=True, verbose_name='Titre formation inter entreprise')),
                ('soustitreF', models.TextField(blank=True, null=True, verbose_name='Sous-titre formation inter entreprise')),
                ('imageF', models.ImageField(blank=True, null=True, upload_to='nossolutions/')),
                ('descriptionF', models.TextField(blank=True, null=True, verbose_name='Description formation inter entreprise')),
                ('voirplusF', models.CharField(blank=True, max_length=255, null=True)),
                ('titreE', models.TextField(blank=True, null=True, verbose_name='Titre Etude de marché')),
                ('soustitreE', models.TextField(blank=True, null=True, verbose_name='Sous-titre Etude de marché')),
                ('imageE', models.ImageField(blank=True, null=True, upload_to='nossolutions/')),
                ('descriptionE', models.TextField(blank=True, null=True, verbose_name='Description Etude de marché')),
                ('voirplusE', models.CharField(blank=True, max_length=255, null=True)),
                ('titreB', models.TextField(blank=True, null=True, verbose_name='Titre Business plan')),
                ('soustitreB', models.TextField(blank=True, null=True, verbose_name='Sous-titre Business plan')),
                ('imageB', models.ImageField(blank=True, null=True, upload_to='nossolutions/')),
                ('descriptionB', models.TextField(blank=True, null=True, verbose_name='Description Business plan')),
                ('voirplusB', models.CharField(blank=True, max_length=255, null=True)),
                ('titreR', models.TextField(blank=True, null=True, verbose_name='Titre Recherche et financement')),
                ('soustitreR', models.TextField(blank=True, null=True, verbose_name='Sous-titre Recherche et financement')),
                ('imageR', models.ImageField(blank=True, null=True, upload_to='nossolutions/')),
                ('descriptionR', models.TextField(blank=True, null=True, verbose_name='Description Recherche et financement')),
                ('voirplusR', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]