# Generated by Django 4.2 on 2023-05-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0026_apropos_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apropos',
            name='label',
            field=models.CharField(blank=True, default='Apropos', max_length=255, null=True),
        ),
    ]
