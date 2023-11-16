# Generated by Django 4.1.7 on 2023-11-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0043_message_motif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='motif',
            field=models.CharField(choices=[('Motif 1', "Avoir d'avantage d’information sur le programmeElevator"), ('Motif 2', 'M’inscrire au programme Elevator')], help_text='Quelle est la raison de votre contact', max_length=1000, null=True),
        ),
    ]
