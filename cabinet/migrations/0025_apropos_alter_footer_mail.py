# Generated by Django 4.2 on 2023-05-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0024_email_footer_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apropos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titreQ', models.CharField(blank=True, max_length=255, null=True, verbose_name='Libellé première section')),
                ('descriptionQ', models.TextField(blank=True, null=True, verbose_name='Description première section')),
                ('imageQ', models.ImageField(blank=True, null=True, upload_to='apropos/')),
                ('titreM', models.CharField(blank=True, max_length=255, null=True, verbose_name='Libellé deuxième section')),
                ('descriptionM', models.TextField(blank=True, null=True, verbose_name='Description deuxième section')),
                ('imageM', models.ImageField(blank=True, null=True, upload_to='apropos/')),
                ('titreV', models.CharField(blank=True, max_length=255, null=True, verbose_name='Libellé troisième section')),
                ('descriptionV', models.TextField(blank=True, null=True, verbose_name='Description troisième section')),
                ('imageV', models.ImageField(blank=True, null=True, upload_to='apropos/')),
                ('titreVa', models.CharField(blank=True, max_length=255, null=True, verbose_name='Libellé quatrième section')),
                ('descriptionVa', models.TextField(blank=True, null=True, verbose_name='Description quatrième section')),
                ('imageVa', models.ImageField(blank=True, null=True, upload_to='apropos/')),
                ('titreE', models.CharField(blank=True, max_length=255, null=True, verbose_name='Libellé cinquième section')),
                ('descriptionE', models.TextField(blank=True, null=True, verbose_name='Description cinquième section')),
                ('imageE', models.ImageField(blank=True, null=True, upload_to='apropos/')),
            ],
        ),
        migrations.AlterField(
            model_name='footer',
            name='mail',
            field=models.ManyToManyField(blank=True, help_text='Pour selectionner plusieurs, appuyer sur la touche ctrl', null=True, to='cabinet.email'),
        ),
    ]
