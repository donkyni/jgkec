from django.contrib import admin

from cabinet.models import Contact, Article, Activite


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'fonction', 'objet', 'date')
    list_filter = ('nom', 'fonction', 'objet', 'date')
    ordering = ('nom', 'fonction', 'objet', 'date')
    search_fields = ('nom', 'fonction', 'objet', 'date')


admin.site.register(Contact, ContactAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'image', 'archive')
    list_filter = ('titre', 'date', 'archive')
    ordering = ('titre', 'date', 'archive')
    search_fields = ('titre', 'texte', 'date', 'archive')


admin.site.register(Article, ArticleAdmin)


class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'image', 'archive')
    list_filter = ('titre', 'date', 'archive')
    ordering = ('titre', 'date', 'archive')
    search_fields = ('titre', 'texte', 'date', 'archive')


admin.site.register(Activite, ActiviteAdmin)
