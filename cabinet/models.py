from django import forms
from django.db import models

# Create your models here.


class Contact(models.Model):
    prenom = models.CharField(max_length=255, null=True, blank=True, verbose_name="Prénom")
    nom = models.CharField(max_length=255, null=True, blank=False, verbose_name="Nom")
    fonction = models.CharField(max_length=255, null=True, blank=False, verbose_name="Fonction")
    objet = models.CharField(max_length=255, null=True, blank=False, verbose_name="Objet")
    message = models.TextField(verbose_name="Message", null=True, blank=False)
    date = models.DateTimeField(null=True, auto_now_add=True, blank=True)
