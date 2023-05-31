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
"""


# ############### PAGE ACCUEIL ##################


class BanniereAccueil(models.Model):
    label = models.CharField(max_length=255, null=True, blank=True, default="BanniereAccueil")
    image = models.ImageField(blank=True, null=True, upload_to="bannieres/")
    titre = models.CharField(max_length=255, null=True, blank=True)
    libelle = models.TextField(verbose_name="Libellé bannière", null=True, blank=True)
    voirplus = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


class Mission(models.Model):
    label = models.CharField(max_length=255, null=True, blank=True, default="Mission")
    titre = models.CharField(max_length=255, null=True, blank=True)
    libellemission = models.TextField(verbose_name="Libellé mission", null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="missions/")
    productivite = models.TextField(verbose_name="Libellé productivite", null=True, blank=True)
    voirplus = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


class LibelleSolution(models.Model):
    label = models.CharField(max_length=255, null=True, blank=True, default="LibelleSolution")
    libelle = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        if self.libelle is None:
            return "ERROR-LIBELLE IS NULL"
        return self.libelle


class Solution(models.Model):
    label = models.CharField(max_length=255, null=True, blank=True, default="Solution")
    titre = models.CharField(max_length=255, null=True, blank=True)
    libelle = models.ManyToManyField(LibelleSolution, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


"""
Pour le footer
"""


class Tel(models.Model):
    label = models.CharField(max_length=255, null=True, blank=True, default="Tel")
    tel = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.tel


class Email(models.Model):
    label = models.CharField(max_length=255, null=True, blank=True, default="mail")
    mail = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    archive = models.BooleanField(default=False)

    def __str__(self):
        return self.mail


class Footer(models.Model):
    label = models.CharField(max_length=255, null=True, blank=True, default="Footer")
    jgkec = models.CharField(max_length=255, null=True, blank=True)
    tel = models.ManyToManyField(Tel, null=True, blank=True)
    mail = models.ManyToManyField(Email, null=True, blank=True,
                                  help_text="Pour selectionner plusieurs, appuyer sur la touche ctrl")
    date = models.DateTimeField(auto_now_add=True, null=True)

# ############### PAGE APROPOS ##################


class Apropos(models.Model):
    label = models.CharField(default="Apropos", max_length=255, null=True, blank=True)

    """
    Qui sommes nous ?
    """
    titreQ = models.CharField(max_length=255, null=True, blank=True, verbose_name="Libellé première section")
    descriptionQ = models.TextField(null=True, blank=True, verbose_name="Description première section")
    imageQ = models.ImageField(null=True, blank=True, upload_to="apropos/")

    """
    Notre mission
    """
    titreM = models.CharField(max_length=255, null=True, blank=True, verbose_name="Libellé deuxième section")
    descriptionM = models.TextField(null=True, blank=True, verbose_name="Description deuxième section")
    imageM = models.ImageField(null=True, blank=True, upload_to="apropos/")

    """
    Notre vision 
    """
    titreV = models.CharField(max_length=255, null=True, blank=True, verbose_name="Libellé troisième section")
    descriptionV = models.TextField(null=True, blank=True, verbose_name="Description troisième section")
    imageV = models.ImageField(null=True, blank=True, upload_to="apropos/")

    """
    Nos valeurs 
    """
    titreVa = models.CharField(max_length=255, null=True, blank=True, verbose_name="Libellé quatrième section")
    descriptionVa = models.TextField(null=True, blank=True, verbose_name="Description quatrième section")
    imageVa = models.ImageField(null=True, blank=True, upload_to="apropos/")

    """
    Notre expertise 
    """
    titreE = models.CharField(max_length=255, null=True, blank=True, verbose_name="Libellé cinquième section")
    descriptionE = models.TextField(null=True, blank=True, verbose_name="Description cinquième section")
    imageE = models.ImageField(null=True, blank=True, upload_to="apropos/")


class NosSolutions(models.Model):
    label = models.CharField(default="NosSolutions", max_length=255, null=True, blank=True)
    titrepage = models.TextField(null=True, blank=True, verbose_name="Titre de la page")

    """
    Programme Diamond
    """
    titreD = models.TextField(null=True, blank=True, verbose_name="Titre programme Diamond")
    soustitreD = models.TextField(null=True, blank=True, verbose_name="Sous-titre programme Diamond")
    imageD = models.ImageField(null=True, blank=True, upload_to="nossolutions/", verbose_name="Image")
    descriptionD = models.TextField(null=True, blank=True, verbose_name="Description programme Diamond")
    voirplusD = models.CharField(max_length=255, null=True, blank=True, verbose_name="Voir plus")

    """
    Formation inter entreprise
    """
    titreF = models.TextField(null=True, blank=True, verbose_name="Titre formation inter entreprise")
    soustitreF = models.TextField(null=True, blank=True, verbose_name="Sous-titre formation inter entreprise")
    imageF = models.ImageField(null=True, blank=True, upload_to="nossolutions/", verbose_name="Image")
    descriptionF = models.TextField(null=True, blank=True, verbose_name="Description formation inter entreprise")
    voirplusF = models.CharField(max_length=255, null=True, blank=True, verbose_name="Voir plus")

    """
    Etude de marché
    """
    titreE = models.TextField(null=True, blank=True, verbose_name="Titre Etude de marché")
    soustitreE = models.TextField(null=True, blank=True, verbose_name="Sous-titre Etude de marché")
    imageE = models.ImageField(null=True, blank=True, upload_to="nossolutions/", verbose_name="Image")
    descriptionE = models.TextField(null=True, blank=True, verbose_name="Description Etude de marché")
    voirplusE = models.CharField(max_length=255, null=True, blank=True, verbose_name="Voir plus")

    """
    Business plan
    """
    titreB = models.TextField(null=True, blank=True, verbose_name="Titre Business plan")
    soustitreB = models.TextField(null=True, blank=True, verbose_name="Sous-titre Business plan")
    imageB = models.ImageField(null=True, blank=True, upload_to="nossolutions/", verbose_name="Image")
    descriptionB = models.TextField(null=True, blank=True, verbose_name="Description Business plan")
    voirplusB = models.CharField(max_length=255, null=True, blank=True, verbose_name="Voir plus")

    """
    Recherche et financement
    """
    titreR = models.TextField(null=True, blank=True, verbose_name="Titre Recherche et financement")
    soustitreR = models.TextField(null=True, blank=True, verbose_name="Sous-titre Recherche et financement")
    imageR = models.ImageField(null=True, blank=True, upload_to="nossolutions/", verbose_name="Image")
    descriptionR = models.TextField(null=True, blank=True, verbose_name="Description Recherche et financement")
    voirplusR = models.CharField(max_length=255, null=True, blank=True, verbose_name="Voir plus")

