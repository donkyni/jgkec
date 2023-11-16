from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact, Article, Activite, Footer, Tel, Solution, Mission, BanniereAccueil, LibelleSolution, Email, \
    Apropos, NosSolutions, HistoriqueActivite, Financement, Diamond, Productivite, Valeur, NotreMission, Expertise, \
    MotDuDG, Performance, Message


# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'mail', 'telephone', 'pays', 'date', 'archive',)
    list_filter = ('nom', 'mail', 'telephone', 'pays', 'date', 'archive')
    ordering = ('nom', 'mail', 'pays', 'date')
    search_fields = ('nom', 'mail', 'pays', 'date')


admin.site.register(Message, MessageAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'fonction', 'objet', 'telephone', 'lu', 'date', 'archive', 'collapse',)
    list_filter = ('nom', 'fonction', 'objet', 'lu', 'date', 'archive')
    ordering = ('nom', 'fonction', 'objet', 'date')
    search_fields = ('nom', 'fonction', 'objet', 'date')


admin.site.register(Contact, ContactAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'image', 'vues', 'archive')
    list_filter = ('titre', 'date', 'vues', 'archive')
    ordering = ('titre', 'date', 'archive')
    search_fields = ('titre', 'texte', 'date', 'archive')


admin.site.register(Article, ArticleAdmin)


class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'image', 'vues', 'archive')
    list_filter = ('titre', 'date', 'vues', 'archive')
    ordering = ('titre', 'date', 'archive')
    search_fields = ('titre', 'texte', 'date', 'archive')


admin.site.register(Activite, ActiviteAdmin)


class HistoriqueActiviteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'image', 'vues', 'archive')
    list_filter = ('titre', 'date', 'vues', 'archive')
    ordering = ('titre', 'date', 'archive')
    search_fields = ('titre', 'texte', 'date', 'archive')


admin.site.register(HistoriqueActivite, HistoriqueActiviteAdmin)


class BanniereAccueilAdmin(admin.ModelAdmin):
    list_display = ('titre', 'libelle', 'image', 'voirplus', 'date')
    list_filter = ('titre', 'libelle', 'image', 'voirplus', 'date')
    ordering = ('titre', 'libelle', 'image', 'voirplus', 'date')
    search_fields = ('titre', 'libelle', 'image', 'voirplus', 'date')
    # summernote_fields = ('libelle',)


admin.site.register(BanniereAccueil, BanniereAccueilAdmin)


class MotDuDGAdmin(admin.ModelAdmin):
    list_display = ('label', 'image', 'titre', 'libelle', 'voirplus', 'date')
    list_filter = ('image', 'titre', 'libelle', 'voirplus', 'date')
    ordering = ('image', 'titre', 'libelle', 'voirplus', 'date')
    search_fields = ('image', 'titre', 'libelle', 'voirplus', 'date')


admin.site.register(MotDuDG, MotDuDGAdmin)


class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'date')
    list_filter = ('libelle', 'date')
    ordering = ('libelle', 'date')
    search_fields = ('libelle', 'date')


admin.site.register(Expertise, ExpertiseAdmin)


class NotreMissionAdmin(admin.ModelAdmin):
    list_display = ('label', 'titre', 'libelle', 'voirplus', 'date')
    list_filter = ('titre', 'libelle', 'voirplus', 'date')
    ordering = ('titre', 'libelle', 'voirplus', 'date')
    search_fields = ('titre', 'libelle', 'voirplus', 'date')


admin.site.register(NotreMission, NotreMissionAdmin)


class ValeurAdmin(admin.ModelAdmin):
    list_display = ('titre', 'libelle', 'voirplus', 'date')
    list_filter = ('titre', 'libelle', 'voirplus', 'date')
    ordering = ('titre', 'libelle', 'voirplus', 'date')
    search_fields = ('titre', 'libelle', 'voirplus', 'date')


admin.site.register(Valeur, ValeurAdmin)


class ProductiviteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'libelle', 'voirplus', 'date')
    list_filter = ('titre', 'libelle', 'voirplus', 'date')
    ordering = ('titre', 'libelle', 'voirplus', 'date')
    search_fields = ('titre', 'libelle', 'voirplus', 'date')


admin.site.register(Productivite, ProductiviteAdmin)


class DiamondAdmin(admin.ModelAdmin):
    list_display = ('titre', 'libelle', 'voirplus', 'date')
    list_filter = ('titre', 'libelle', 'voirplus', 'date')
    ordering = ('titre', 'libelle', 'voirplus', 'date')
    search_fields = ('titre', 'libelle', 'voirplus', 'date')


admin.site.register(Diamond, DiamondAdmin)


class FinancementAdmin(admin.ModelAdmin):
    list_display = ('titre', 'libelle', 'voirplus', 'date')
    list_filter = ('titre', 'libelle', 'voirplus', 'date')
    ordering = ('titre', 'libelle', 'voirplus', 'date')
    search_fields = ('titre', 'libelle', 'voirplus', 'date')


admin.site.register(Financement, FinancementAdmin)


class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'voirplus', 'date')
    list_filter = ('libelle', 'voirplus', 'date')
    ordering = ('libelle', 'voirplus', 'date')
    search_fields = ('libelle', 'voirplus', 'date')


admin.site.register(Performance, PerformanceAdmin)


class MissionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'libellemission', 'image', 'productivite', 'detailproductivite', 'voirplus',
                    'notreexpertise', 'solution', 'valeur', 'date')
    list_filter = ('titre', 'libellemission', 'image', 'productivite', 'voirplus', 'date')
    ordering = ('titre', 'libellemission', 'image', 'productivite', 'voirplus', 'date')
    search_fields = ('titre', 'libellemission', 'image', 'productivite', 'voirplus', 'date')
    # summernote_fields = ('libellemission', 'productivite',)


admin.site.register(Mission, MissionAdmin)


class LibelleSolutionAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'date')
    list_filter = ('libelle',  'date')
    ordering = ('libelle',  'date')
    search_fields = ('libelle', 'date')


admin.site.register(LibelleSolution, LibelleSolutionAdmin)


class SolutionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date')
    list_filter = ('titre',  'date')
    ordering = ('titre',  'date')
    search_fields = ('titre', 'date')


admin.site.register(Solution, SolutionAdmin)


class TelAdmin(admin.ModelAdmin):
    list_display = ('tel', 'date', 'archive')
    list_filter = ('tel', 'date', 'archive')
    ordering = ('tel', 'date', 'archive')
    search_fields = ('tel', 'date', 'archive')


admin.site.register(Tel, TelAdmin)


class EmailAdmin(admin.ModelAdmin):
    list_display = ('mail', 'date', 'archive')
    list_filter = ('mail', 'date', 'archive')
    ordering = ('mail', 'date', 'archive')
    search_fields = ('mail', 'date', 'archive')


admin.site.register(Email, EmailAdmin)


class FooterAdmin(admin.ModelAdmin):
    list_display = ('jgkec', 'date')
    list_filter = ('jgkec', 'date')
    ordering = ('jgkec', 'date')
    search_fields = ('jgkec', 'date')


admin.site.register(Footer, FooterAdmin)


class AproposAdmin(admin.ModelAdmin):
    list_display = ('titreQ', 'descriptionQ', 'imageQ',
                    'titreM', 'descriptionM', 'imageM',
                    'titreV', 'descriptionV', 'imageV',
                    'titreVa', 'descriptionVa', 'imageVa',
                    'titreE', 'descriptionE', 'imageE')
    list_filter = ('titreQ', 'titreM', 'titreV', 'titreVa', 'titreE')
    ordering = ('titreQ', 'titreM', 'titreV', 'titreVa', 'titreE')
    search_fields = ('titreQ', 'titreM', 'titreV', 'titreVa', 'titreE')


admin.site.register(Apropos, AproposAdmin)


class NosSolutionsAdmin(admin.ModelAdmin):
    list_display = ('titrepage',
                    'titreD','soustitreD', 'imageD', 'descriptionD', 'voirplusD',
                    'titreF','soustitreF', 'imageF', 'descriptionF', 'voirplusF',
                    'titreE','soustitreE', 'imageE', 'descriptionE', 'voirplusE',
                    'titreB','soustitreB', 'imageB', 'descriptionB', 'voirplusB',
                    'titreR','soustitreR', 'imageR', 'descriptionR', 'voirplusR')
    list_filter = ('titreD', 'titreF', 'titreE', 'titreB', 'titreR')
    ordering = ('titreD', 'titreF', 'titreE', 'titreB', 'titreR')
    search_fields = ('titreD', 'titreF', 'titreE', 'titreB', 'titreR')


admin.site.register(NosSolutions, NosSolutionsAdmin)