# Generated by Django 4.1.7 on 2023-09-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0037_mission_mot_des_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diamond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='Diamond', max_length=255, null=True)),
                ('titre', models.TextField(blank=True, null=True, verbose_name='Titre Diamond')),
                ('libelle', models.TextField(blank=True, null=True, verbose_name='Libellé Diamond')),
                ('voirplus', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='Expertise', max_length=255, null=True)),
                ('titre', models.TextField(blank=True, null=True, verbose_name='Titre Expertise')),
                ('libelle', models.TextField(blank=True, null=True, verbose_name='Libellé Expertise')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Financement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='Financement', max_length=255, null=True)),
                ('titre', models.TextField(blank=True, null=True, verbose_name='Titre Financement')),
                ('libelle', models.TextField(blank=True, null=True, verbose_name='Libellé Financement')),
                ('voirplus', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MotDuDG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='Expertise', max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='motdudg/')),
                ('titre', models.TextField(blank=True, null=True, verbose_name='Titre mot du DG')),
                ('libelle', models.TextField(blank=True, null=True, verbose_name='Libellé mot du DG')),
                ('voirplus', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotreMission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='Mission', max_length=255, null=True)),
                ('titre', models.TextField(blank=True, null=True, verbose_name='Titre mission')),
                ('libelle', models.TextField(blank=True, null=True, verbose_name='Libellé mission')),
                ('voirplus', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='Performance', max_length=255, null=True)),
                ('libelle', models.TextField(blank=True, null=True, verbose_name='Libellé Performance')),
                ('voirplus', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productivite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='Productivite', max_length=255, null=True)),
                ('titre', models.TextField(blank=True, null=True, verbose_name='Titre productivité')),
                ('libelle', models.TextField(blank=True, null=True, verbose_name='Libellé productivité')),
                ('voirplus', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Valeur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='Valeur', max_length=255, null=True)),
                ('titre', models.TextField(blank=True, null=True, verbose_name='Titre Valeur')),
                ('libelle', models.TextField(blank=True, null=True, verbose_name='Libellé Valeur')),
                ('voirplus', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
