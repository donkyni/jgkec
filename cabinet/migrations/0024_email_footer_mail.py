# Generated by Django 4.2 on 2023-05-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0023_rename_libelle_mission_libellemission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='mail', max_length=255, null=True)),
                ('mail', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('archive', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='footer',
            name='mail',
            field=models.ManyToManyField(blank=True, null=True, to='cabinet.email'),
        ),
    ]
