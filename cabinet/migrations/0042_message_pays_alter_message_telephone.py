# Generated by Django 4.1.7 on 2023-11-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0041_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='pays',
            field=models.CharField(max_length=255, null=True, verbose_name='Pays'),
        ),
        migrations.AlterField(
            model_name='message',
            name='telephone',
            field=models.CharField(default='(+000) 12345678', max_length=15, null=True, verbose_name='Numéro de téléphone'),
        ),
    ]