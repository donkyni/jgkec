# Generated by Django 4.1.7 on 2023-11-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0042_message_pays_alter_message_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='motif',
            field=models.CharField(choices=[('Avoir davantage d’information sur le programme Elevator', 'Avoir davantage d’information sur le programme Elevator'), ('M’inscrire au programme Elevator', 'M’inscrire au programme Elevator')], help_text='Quelle est la raison de votre contact', max_length=1000, null=True),
        ),
    ]
