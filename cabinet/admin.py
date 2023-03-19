from django.contrib import admin

from cabinet.models import Contact


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'fonction', 'objet', 'message')
    list_filter = ('nom', 'fonction', 'objet')
    ordering = ('nom', 'fonction', 'objet')
    search_fields = ('nom', 'fonction', 'objet')


admin.site.register(Contact, ContactAdmin)
