# Generated by Django 5.0.1 on 2024-01-10 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0052_remove_message_motif'),
    ]

    operations = [
        migrations.AddField(
            model_name='motdudg',
            name='terme',
            field=models.TextField(blank=True, null=True, verbose_name='Termes et conditions'),
        ),
    ]
