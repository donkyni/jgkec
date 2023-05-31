import uuid

from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from cabinet.models import Contact, Activite, Article, BanniereAccueil, Mission, LibelleSolution, Solution, Tel, Footer, \
    Email, Apropos, NosSolutions


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['prenom', 'nom', 'fonction', 'objet', 'message', 'telephone']
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


class DeleteMessage(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('lu',)


class BanniereAccueilForm(forms.ModelForm):
    class Meta:
        model = BanniereAccueil

        from django_summernote.fields import SummernoteTextField
        libelle = SummernoteTextField()
        fields = ['label', 'image', 'titre', 'libelle', 'voirplus']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'libelle': SummernoteWidget(),
        }
        enctype = 'multipart/form-data'


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['label', 'titre', 'libellemission', 'image', 'productivite', 'voirplus']
        widgets = {
            'libellemission': SummernoteWidget(),
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
            'productivite': SummernoteWidget(),
            'label': forms.TextInput(attrs={'disabled': 'true'})
        }
        enctype = 'multipart/form-data'


class LibelleSolutionForm(forms.ModelForm):
    class Meta:
        model = LibelleSolution
        fields = '__all__'
        widgets = {
            'label': forms.TextInput(attrs={'disabled': 'true'})
        }


class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = '__all__'
        widgets = {
            'label': forms.TextInput(attrs={'disabled': 'true'})
        }


class TelForm(forms.ModelForm):
    class Meta:
        model = Tel
        fields = '__all__'
        widgets = {
            'label': forms.TextInput(attrs={'disabled': 'true'})
        }


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        widgets = {
            'label': forms.TextInput(attrs={'disabled': 'true'})
        }


class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = '__all__'
        widgets = {
            'label': forms.TextInput(attrs={'disabled': 'true'}),
        }


"""
Page APROPOS
"""


class AproposForm(forms.ModelForm):
    class Meta:
        model = Apropos
        fields = ['label',
                  'titreQ', 'descriptionQ', 'imageQ',
                  'titreM', 'descriptionM', 'imageM',
                  'titreV', 'descriptionV', 'imageV',
                  'titreVa', 'descriptionVa', 'imageVa',
                  'titreE', 'descriptionE', 'imageE']
        widgets = {
            'descriptionQ': SummernoteWidget(),
            'descriptionM': SummernoteWidget(),
            'descriptionV': SummernoteWidget(),
            'descriptionVa': SummernoteWidget(),
            'descriptionE': SummernoteWidget(),
            'imageQ': forms.ClearableFileInput(attrs={'multiple': True}),
            'imageM': forms.ClearableFileInput(attrs={'multiple': True}),
            'imageV': forms.ClearableFileInput(attrs={'multiple': True}),
            'imageVa': forms.ClearableFileInput(attrs={'multiple': True}),
            'imageE': forms.ClearableFileInput(attrs={'multiple': True}),
            'label': forms.TextInput(attrs={'disabled': 'true'})
        }
        enctype = 'multipart/form-data'


"""
Page NOS SOLUTIONS
"""


class NosSolutionsForm(forms.ModelForm):
    class Meta:
        model = NosSolutions
        fields = ['label', 'titrepage',
                  'titreD', 'soustitreD', 'imageD', 'descriptionD', 'voirplusD',
                  'titreF', 'soustitreF', 'imageF', 'descriptionF', 'voirplusF',
                  'titreE', 'soustitreE', 'imageE', 'descriptionE', 'voirplusE',
                  'titreB', 'soustitreB', 'imageB', 'descriptionB', 'voirplusB',
                  'titreR', 'soustitreR', 'imageR', 'descriptionR', 'voirplusR']
        widgets = {
            'titrepage': SummernoteWidget(),
            'titreD': SummernoteWidget(),
            'titreF': SummernoteWidget(),
            'titreE': SummernoteWidget(),
            'titreB': SummernoteWidget(),
            'titreR': SummernoteWidget(),
            'soustitreD': SummernoteWidget(),
            'soustitreF': SummernoteWidget(),
            'soustitreE': SummernoteWidget(),
            'soustitreB': SummernoteWidget(),
            'soustitreR': SummernoteWidget(),
            'descriptionD': SummernoteWidget(),
            'descriptionF': SummernoteWidget(),
            'descriptionE': SummernoteWidget(),
            'descriptionB': SummernoteWidget(),
            'descriptionR': SummernoteWidget(),
            'imageD': forms.ClearableFileInput(attrs={'multiple': True}),
            'imageF': forms.ClearableFileInput(attrs={'multiple': True}),
            'imageE': forms.ClearableFileInput(attrs={'multiple': True}),
            'imageB': forms.ClearableFileInput(attrs={'multiple': True}),
            'imageR': forms.ClearableFileInput(attrs={'multiple': True}),
            'label': forms.TextInput(attrs={'disabled': 'true'})
        }
        enctype = 'multipart/form-data'
