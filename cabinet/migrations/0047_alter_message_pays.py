# Generated by Django 4.1.7 on 2023-11-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0046_message_code_pays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pays',
            field=models.CharField(choices=[('France', '+33'), ('Afghanistan', '+93')], max_length=255, null=True, verbose_name='Pays'),
        ),
    ]