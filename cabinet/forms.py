import uuid

from django import forms
from django_summernote.widgets import SummernoteWidget
from cabinet.models import Contact, Activite, Article, BanniereAccueil, Mission, LibelleSolution, Solution, Tel, Footer, \
    Email, Apropos, NosSolutions, MotDuDG, Financement, Diamond, Productivite, Valeur, NotreMission, Expertise, \
    Performance, Message

from django_summernote.fields import SummernoteTextField


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['motif', 'nom', 'prenom', 'mail', 'pays', 'code_pays', 'telephone']
        widgets = {
            'motif': forms.Select(),
            'mail': forms.EmailInput(),
            'pays': forms.Select(attrs={'id': 'id_pays'}),
            'code_pays': forms.Select(attrs={'id': 'id_code_pays'}),
        }


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
            'titre': SummernoteWidget(),
            'texte': SummernoteWidget(),

        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'texte', 'image']
        widgets = {
            'titre': SummernoteWidget(),
            'texte': SummernoteWidget(),

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

            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'libelle': SummernoteWidget(),
        }
        enctype = 'multipart/form-data'


class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance

        libelle = SummernoteTextField()

        fields = ['label', 'libelle', 'voirplus']
        widgets = {

            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'libelle': SummernoteWidget(),
        }


class ExpertiseForm(forms.ModelForm):
    class Meta:
        model = Expertise

        libelle = SummernoteTextField()

        fields = ['label', 'libelle']
        widgets = {

            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'libelle': SummernoteWidget(),
        }


class NotreMissionForm(forms.ModelForm):
    class Meta:
        model = NotreMission

        titre = SummernoteTextField()
        libelle = SummernoteTextField()

        fields = ['label', 'titre', 'libelle', 'voirplus']
        widgets = {

            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'titre': SummernoteWidget(),
            'libelle': SummernoteWidget(),
        }


class ValeurForm(forms.ModelForm):
    class Meta:
        model = Valeur

        titre = SummernoteTextField()
        libelle = SummernoteTextField()

        fields = ['label', 'titre', 'libelle', 'voirplus']
        widgets = {

            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'titre': SummernoteWidget(),
            'libelle': SummernoteWidget(),
        }


class ProductiviteForm(forms.ModelForm):
    class Meta:
        model = Productivite

        titre = SummernoteTextField()
        libelle = SummernoteTextField()

        fields = ['label', 'titre', 'libelle', 'voirplus']
        widgets = {

            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'titre': SummernoteWidget(),
            'libelle': SummernoteWidget(),
        }


class DiamondForm(forms.ModelForm):
    class Meta:
        model = Diamond

        titre = SummernoteTextField()
        libelle = SummernoteTextField()

        fields = ['label', 'titre', 'libelle', 'voirplus']
        widgets = {

            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'titre': SummernoteWidget(),
            'libelle': SummernoteWidget(),
        }


class FinancementForm(forms.ModelForm):
    class Meta:
        model = Financement

        titre = SummernoteTextField()
        libelle = SummernoteTextField()

        fields = ['label', 'titre', 'libelle', 'voirplus']
        widgets = {

            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'titre': SummernoteWidget(),
            'libelle': SummernoteWidget(),
        }


class MotDuDGForm(forms.ModelForm):
    class Meta:
        model = MotDuDG

        titre = SummernoteTextField()
        libelle = SummernoteTextField()

        fields = ['label', 'image', 'titre', 'libelle', 'voirplus']
        widgets = {

            'label': forms.TextInput(attrs={'disabled': 'true'}),
            'titre': SummernoteWidget(),
            'libelle': SummernoteWidget(),
        }
        enctype = 'multipart/form-data'


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ['label', 'titre', 'libellemission', 'image', 'productivite', 'detailproductivite', 'voirplus',
                  'notreexpertise', 'solution', 'mot_du_dg', 'mot_des_clients', 'niveau_performance', 'valeur']
        widgets = {
            'libellemission': SummernoteWidget(),

            'productivite': SummernoteWidget(),
            'detailproductivite': SummernoteWidget(),
            'notreexpertise': SummernoteWidget(),
            'solution': SummernoteWidget(),
            'valeur': SummernoteWidget(),
            'mot_du_dg': SummernoteWidget(),
            'mot_des_clients': SummernoteWidget(),
            'niveau_performance': SummernoteWidget(),
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
            'label': forms.TextInput(attrs={'disabled': 'true'})
        }
        enctype = 'multipart/form-data'
