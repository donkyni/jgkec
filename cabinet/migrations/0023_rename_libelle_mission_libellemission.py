# Generated by Django 4.2 on 2023-05-25 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0022_banniereaccueil_label_footer_label_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='libelle',
            new_name='libellemission',
        ),
    ]
