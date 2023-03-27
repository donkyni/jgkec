from django.contrib import admin

from cabinet.models import Contact


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'fonction', 'objet', 'message', 'date')
    list_filter = ('nom', 'fonction', 'objet', 'date')
    ordering = ('nom', 'fonction', 'objet', 'date')
    search_fields = ('nom', 'fonction', 'objet', 'date')


admin.site.register(Contact, ContactAdmin)
