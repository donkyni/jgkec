from django import forms

from cabinet.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('prenom', 'nom', 'fonction', 'objet', 'message',)
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 10})
        }
