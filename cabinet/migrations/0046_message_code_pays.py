# Generated by Django 4.1.7 on 2023-11-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0045_alter_message_motif'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='code_pays',
            field=models.CharField(max_length=255, null=True, verbose_name='Code du Pays'),
        ),
    ]
