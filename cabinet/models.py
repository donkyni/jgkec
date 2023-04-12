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
    archive = models.BooleanField(default=False)


class Article(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True, verbose_name="Titre")
    texte = models.TextField(verbose_name="Texte", null=True, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to="articles")
    date = models.DateTimeField(null=True, auto_now_add=True, blank=True)
    archive = models.BooleanField(default=False)


class Activite(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="activites")
    titre = models.CharField(max_length=255, null=True, blank=True, verbose_name="Titre")
    texte = models.TextField(verbose_name="Texte", null=True, blank=False)
    date = models.DateTimeField(null=True, auto_now_add=True, blank=True)
    archive = models.BooleanField(default=False)
