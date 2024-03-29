# Generated by Django 4.1.7 on 2024-01-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0048_alter_message_pays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Prénom')),
                ('nom', models.CharField(max_length=255, null=True, verbose_name='Nom')),
                ('datenaiss', models.DateField(blank=True, null=True)),
                ('pays', models.CharField(max_length=255, null=True, verbose_name='Pays')),
                ('mail', models.EmailField(max_length=254, null=True, verbose_name='Adresse email')),
                ('telephone', models.CharField(default='(+000) 12345678', max_length=15, null=True, verbose_name='Numéro de téléphone')),
                ('titreposte', models.CharField(max_length=255, null=True, verbose_name='Titre du poste')),
                ('entreprise', models.CharField(max_length=255, null=True, verbose_name="Nom de l'entreprise/organisation")),
                ('secteur', models.CharField(max_length=255, null=True, verbose_name="Secteur d'activité")),
                ('experience', models.CharField(max_length=255, null=True, verbose_name="Nombre d'année d'expérience professionnelle")),
                ('detail', models.CharField(choices=[('Réseaux sociaux', 'Réseaux sociaux'), ('Site web JGK-EC', 'Site web JGK-EC'), ('Bouche-à-oreille', 'Bouche-à-oreille'), ('Autre (veuillez préciser)', 'Autre (veuillez préciser)')], max_length=255, null=True, verbose_name='Comment avez-vous entendu parler du Programme Elevator ?')),
                ('pourquoi', models.TextField(null=True, verbose_name='Pourquoi souhaitez-vous rejoindre le Programme Elevator ?')),
                ('objectifs', models.TextField(null=True, verbose_name='•\tQuels sont vos objectifs professionnels ?')),
                ('confirmation', models.BooleanField(null=True, verbose_name='Veuillez confirmer votre disponibilité pour les sessions en soirée.')),
                ('terme', models.BooleanField(null=True, verbose_name='Acceptez-vous les termes et conditions du Programme Elevator ? [Lien vers les termes et conditions')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('archive', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='code_pays',
        ),
    ]
