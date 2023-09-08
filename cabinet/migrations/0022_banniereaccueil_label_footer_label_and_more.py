# Generated by Django 4.2 on 2023-05-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0021_libellesolution_remove_solution_libelle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banniereaccueil',
            name='label',
            field=models.CharField(blank=True, default='BanniereAccueil', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='label',
            field=models.CharField(blank=True, default='Footer', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='libellesolution',
            name='label',
            field=models.CharField(blank=True, default='LibelleSolution', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mission',
            name='label',
            field=models.CharField(blank=True, default='Mission', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='label',
            field=models.CharField(blank=True, default='Solution', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tel',
            name='label',
            field=models.CharField(blank=True, default='Tel', max_length=255, null=True),
        ),
    ]