# Generated by Django 5.0.1 on 2024-01-09 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0051_alter_elevator_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='motif',
        ),
    ]
