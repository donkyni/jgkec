# Generated by Django 4.1.7 on 2023-09-14 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0038_diamond_expertise_financement_motdudg_notremission_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expertise',
            name='titre',
        ),
    ]
