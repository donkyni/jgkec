from django import forms

from cabinet.models import Contact, Activite, Article


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('prenom', 'nom', 'fonction', 'objet', 'message',)
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 10})
        }


class ActiviteForm(forms.ModelForm):
    class Meta:
        model = Activite
        fields = ('image', 'titre', 'texte',)
        widgets = {
            'texte': forms.Textarea(attrs={'cols': 50, 'rows': 10})
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'texte', 'image']
        widgets = {
            'texte': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
            'image': forms.ClearableFileInput(attrs={'multiple': True})
        }
        enctype = 'multipart/form-data'
