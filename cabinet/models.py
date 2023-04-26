import uuid

from django.db import models


class Contact(models.Model):
    collapse = models.UUIDField(default=uuid.uuid4, editable=False)
    prenom = models.CharField(max_length=255, null=True, blank=True, verbose_name="Prénom")
    nom = models.CharField(max_length=255, null=True, blank=False, verbose_name="Nom")
    fonction = models.CharField(max_length=255, null=True, blank=False, verbose_name="Fonction")
    objet = models.CharField(max_length=255, null=True, blank=False, verbose_name="Objet")
    message = models.TextField(verbose_name="Message", null=True, blank=False)
    telephone = models.CharField(verbose_name="Numéro de téléphone", max_length=13, null=True, default="228xxxxxxxx")
    lu = models.BooleanField(default=False, verbose_name="Cochez le message")
    date = models.DateTimeField(null=True, auto_now_add=True, blank=True)
    archive = models.BooleanField(default=False)


class Article(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True, verbose_name="Titre")
    texte = models.TextField(verbose_name="Texte", null=True, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to="articles/")
    date = models.DateTimeField(null=True, auto_now_add=True, blank=True)
    vues = models.IntegerField(null=True, default=0)
    archive = models.BooleanField(default=False)


class Activite(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="articles/")
    titre = models.CharField(max_length=255, null=True, blank=True, verbose_name="Titre")
    texte = models.TextField(verbose_name="Texte", null=True, blank=False)
    date = models.DateTimeField(null=True, auto_now_add=True, blank=True)
    vues = models.IntegerField(null=True, default=0)
    archive = models.BooleanField(default=False)


"""
Cette section concerne la modification 
des differentes sections sur les pages



class Accueil(models.Model):
    banniere_accueil = models.TextField(verbose_name="Bannière déroulante", null=True, blank=False)
    notre_mission = models.TextField(verbose_name="Bannière notre mission", null=True, blank=False)
    image_productivite = models.ImageField(verbose_name="Image boostez votre productivité", blank=True, null=True, upload_to="accueil")
    texte_productivite = models.TextField(verbose_name="Texte boostez votre productivité", null=True, blank=False)
    nos_solutions = models.TextField(verbose_name="Texte nos solutions", null=True, blank=False)

"""