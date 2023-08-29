# Generated by Django 4.2 on 2023-05-15 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0019_banniereaccueil_mission_solution_tel_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='banniereaccueil',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='mission',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='solution',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tel',
            name='archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tel',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
