# Generated by Django 4.1.7 on 2023-09-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0034_mission_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='valeur',
            field=models.TextField(blank=True, null=True, verbose_name='Nos valeurs'),
        ),
    ]