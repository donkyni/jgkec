# Generated by Django 4.1.7 on 2024-01-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0049_elevator_remove_message_code_pays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elevator',
            name='datenaiss',
            field=models.DateField(blank=True, null=True, verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='elevator',
            name='objectifs',
            field=models.TextField(null=True, verbose_name='Quels sont vos objectifs professionnels ?'),
        ),
        migrations.AlterField(
            model_name='elevator',
            name='terme',
            field=models.BooleanField(null=True, verbose_name='Acceptez-vous les termes et conditions du Programme Elevator ?'),
        ),
    ]
