from _ast import arg

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.forms import formset_factory
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from cabinet.forms import ContactForm, ArticleForm, ActiviteForm, DeleteMessage, BanniereAccueilForm, MissionForm, \
    FooterForm, AproposForm, NosSolutionsForm, PerformanceForm, MotDuDGForm, ExpertiseForm, ValeurForm, \
    NotreMissionForm, ProductiviteForm, DiamondForm, FinancementForm, MessageForm, ElevatorForm
from cabinet.models import Article, Activite, Contact, BanniereAccueil, Mission, Solution, Footer, Apropos, \
    NosSolutions, HistoriqueActivite, Performance, MotDuDG, Expertise, Valeur, NotreMission, Productivite, Diamond, \
    Financement, Message
from django.contrib.auth.models import User

from django.utils import timezone
from django.contrib.auth import authenticate, login, logout


def time_diff(date):
    now = timezone.now().astimezone(timezone.utc)
    diff = now - date
    seconds = diff.seconds
    days = diff.days

    if days > 365:
        return f"Il y'a {days // 365} an{'s' if days // 365 > 1 else ''}"
    elif days > 30:
        return f"Il y'a {days // 30} mois"
    elif days > 0:
        return f"Il y'a {days} jour{'s' if days > 1 else ''}"
    elif seconds > 3600:
        return f"Il y'a {seconds // 3600} heure{'s' if seconds // 3600 > 1 else ''}"
    elif seconds > 60:
        return f"Il y'a {seconds // 60} minute{'s' if seconds // 60 > 1 else ''}"
    else:
        return "Il y'a 1 seconde"


def login_url(request):
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe invalide')
        else:
            messages.error(request, 'Formulaire invalide')
    return render(request, 'login.html', locals())


def logout_url(request):
    logout(request)
    return redirect('acceuil')


def save_all(request, form, template_name, model, template_name2, mycontext):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            if model == "articleadmin":
                form.save()
                data['form_is_valid'] = True
                data[model] = render_to_string(template_name2, mycontext)
        else:
            data['form_is_valid'] = False

    context = {
        'form': form
    }
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def acceuil(request):
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    banniereAccueil = BanniereAccueil.objects.get(label="BanniereAccueil")
    mission = Mission.objects.get(label="Mission")

    notremission = NotreMission.objects.get(label="NotreMission")
    valeur = Valeur.objects.get(label="Valeur")
    productivite = Productivite.objects.get(label="Productivite")
    diamond = Diamond.objects.get(label="Diamond")
    financement = Financement.objects.get(label="Financement")
    expertise = Expertise.objects.get(label="Expertise")
    motdudg = MotDuDG.objects.get(label="MotDuDG")
    performance = Performance.objects.get(label="Performance")

    footer = Footer.objects.filter(label="Footer")
    return render(request, 'acceuil.html', locals())


def contacts(request):
    return render(request, 'contacts.html', locals())


def expertise(request):
    return render(request, 'expertise/expertise.html', locals())


def ingenierie(request):
    return render(request, 'expertise/ingenierie.html', locals())


def management(request):
    return render(request, 'expertise/management.html', locals())


def finance(request):
    return render(request, 'expertise/financement.html', locals())


"""
def developpement(request):
    return render(request, 'expertise/developpement.html', locals())
"""


def reprise(request):
    return render(request, 'expertise/reprise.html', locals())


def etude(request):
    return render(request, 'expertise/etude.html', locals())


def insertion(request):
    return render(request, 'expertise/insertion.html', locals())


def formation(request):
    return render(request, 'formation/formations.html', locals())


def formule(request):
    fileurl = " "
    filename = " "
    if request.method == 'POST':
        f = request.FILES['file']
        fs = FileSystemStorage()
        filename, ext = str(f).split('.')
        file = fs.save(str(f), f)
        fileurl = fs.url(file)
        size = fs.size(file)

    saveurl = "/fichier_static/2_Formulaire%20d'inscription%2004%20postures_2wI9KF5.pdf"
    savename = "2_Formulaire d'inscription 04 postures"
    saveurl2 = "/fichier_static/Donald-Pr%C3%A9sentation%20Programme%20DIAMOND.pdf"
    savename2 = "Plaquette de présentation"
    saveurl3 = "/fichier_static/3_Formulaire%20d'inscription%2004%20postures_t5nyz9Q.pdf"
    savename3 = "3_Formulaire d'inscription 04 postures"

    return render(request, 'formation/formule.html', locals())


def calendrier(request):
    saveurl = "/fichier_static/2_Formulaire%20d'inscription%2004%20postures_2wI9KF5.pdf"
    savename = "2_Formulaire d'inscription 04 postures"
    saveurl3 = "/fichier_static/3_Formulaire%20d'inscription%2004%20postures_t5nyz9Q.pdf"
    savename3 = "3_Formulaire d'inscription 04 postures"

    return render(request, 'formation/calendrier.html', locals())


def calendrier2(request):
    saveurl = "/fichier_static/2_Formulaire%20d'inscription%2004%20postures_2wI9KF5.pdf"
    savename = "2_Formulaire d'inscription 04 postures"
    saveurl3 = "/fichier_static/3_Formulaire%20d'inscription%2004%20postures_t5nyz9Q.pdf"
    savename3 = "3_Formulaire d'inscription 04 postures"

    return render(request, 'formation/calendrier2.html', locals())


def sondage(request):
    return render(request, 'sondage/sondage.html', locals())


def solution(request):
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    nossolutions = NosSolutions.objects.get(label="NosSolutions")
    mission = Mission.objects.get(label="Mission")
    footer = Footer.objects.filter(label="Footer")
    return render(request, 'solution/solution.html', locals())


def activite(request):
    activites = Activite.objects.filter(archive=False).order_by('-date')
    historiques_activites = HistoriqueActivite.objects.filter(archive=True).order_by('-date')
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    footer = Footer.objects.filter(label="Footer")
    mission = Mission.objects.get(label="Mission")

    context = {
        'activites': activites,
        'historiques_activites': historiques_activites,
        'articles_count': articles_count,
        'activites_count': activites_count,
        "footer": footer,
        "mission": mission,
    }
    return render(request, 'activite/activite.html', context)


def article(request):
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    articles = Article.objects.filter(archive=False).order_by('-date')
    footer = Footer.objects.filter(label="Footer")
    mission = Mission.objects.get(label="Mission")

    context = {
        "articles": articles,
        "articles_count": articles_count,
        "activites_count": activites_count,
        "footer": footer,
        "mission": mission,
    }
    return render(request, 'article/article.html', context)


def apropos(request):
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    propos = Apropos.objects.get(label="Apropos")
    footer = Footer.objects.filter(label="Footer")
    mission = Mission.objects.get(label="Mission")
    return render(request, 'apropos/apropos.html', locals())


def contacteznous(request):
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    mission = Mission.objects.get(label="Mission")
    footer = Footer.objects.filter(label="Footer")

    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacteznous')
    else:
        form = ContactForm()
    """

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacteznous')
    else:
        form = MessageForm()

    context = {
        'form': form,
        'articles_count': articles_count,
        'activites_count': activites_count,
        "footer": footer,
        "mission": mission,
    }
    return render(request, 'contacteznous/contacteznous.html', context)


def elevator(request):
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    mission = Mission.objects.get(label="Mission")
    footer = Footer.objects.filter(label="Footer")

    if request.method == 'POST':
        e_form = ElevatorForm(request.POST)
        if e_form.is_valid():
            e_form.save()
            return redirect('aftersubmit')
    else:
        e_form = ElevatorForm()

    context = {
        'e_form': e_form,
        'articles_count': articles_count,
        'activites_count': activites_count,
        "footer": footer,
        "mission": mission,
    }
    return render(request, 'contacteznous/elevator.html', context)


def termes(request):
    motdudg = MotDuDG.objects.get(label="MotDuDG")
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    mission = Mission.objects.get(label="Mission")
    footer = Footer.objects.filter(label="Footer")
    return render(request, 'contacteznous/termes.html', locals())


def aftersubmit(request):
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    mission = Mission.objects.get(label="Mission")
    footer = Footer.objects.filter(label="Footer")
    return render(request, 'contacteznous/aftersubmit.html', locals())


def feedback(request):
    activites_count = Activite.objects.filter(archive=False).order_by('-date').count()
    articles_count = Article.objects.filter(archive=False).order_by('-date').count()
    footer = Footer.objects.filter(label="Footer")
    return render(request, 'feedback/feedback.html', locals())


@login_required
def dashboard(request):
    count_articles = Article.objects.filter(archive=False).count()
    count_activites = Activite.objects.filter(archive=False).count()
    # count_contacts = Contact.objects.filter(archive=False).count()
    count_message = Message.objects.filter(archive=False).count()
    trois_derniers_message = Message.objects.filter(archive=False).order_by('-date')[:3]
    admin_count = User.objects.filter(is_staff=True, is_superuser=True).count()
    latest_articles = Article.objects.filter(archive=False).order_by('-date')[:1]
    latest_activites = Activite.objects.filter(archive=False).order_by('-date')[:1]

    # Ajouter la durée pour chaque contact
    for contact in trois_derniers_message:
        contact.time_diff = time_diff(contact.date)

    return render(request, 'dashboard.html', locals())


@login_required
def articleadmin(request):
    articles = Article.objects.filter(archive=False)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('articleadmin')
    else:
        form = ArticleForm()

    context = {
        "articles": articles,
        "form": form
    }
    return render(request, 'articleadmin/articleadmin.html', context)


@login_required
def updatearticleadmin(request, id):
    articles = Article.objects.filter(archive=False)
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articleadmin')
    else:
        form = ArticleForm(instance=article)

    context = {
        "articles": articles,
        "form": form
    }
    return render(request, 'articleadmin/articleadmin.html', context)


@login_required
def deletearticleadmin(request, id):
    data = dict()
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        article.archive = True
        article.save()
        data['form_is_valid'] = True
        articles = Article.objects.filter(archive=False)
        data['articleadmin'] = render_to_string('articleadmin/listarticleadmin.html',
                                                {'articles': articles})
    else:
        context = {
            'article': article,
        }
        data['html_form'] = render_to_string('articleadmin/deletearticleadmin.html', context, request=request)

    return JsonResponse(data)


@login_required
def activiteadmin(request):
    activites = Activite.objects.filter(archive=False)

    if request.method == 'POST':
        form = ActiviteForm(request.POST,
                            request.FILES)
        if form.is_valid():
            form.save()
            redirect('activite')
    else:
        form = ActiviteForm()
    return render(request, 'activiteadmin/activiteadmin.html', locals())


@login_required
def updateactiviteadmin(request, id):
    activites = Activite.objects.filter(archive=False)
    activite = get_object_or_404(Activite, id=id)

    if request.method == "POST":
        form = ActiviteForm(request.POST, request.FILES, instance=activite)
        if form.is_valid():
            form.save()
            return redirect('activiteadmin')
    else:
        form = ActiviteForm(instance=activite)

    context = {
        "activites": activites,
        "form": form
    }
    return render(request, 'activiteadmin/activiteadmin.html', context)


@login_required
def deleteactiviteadmin(request, id):
    data = dict()
    activite = get_object_or_404(Activite, id=id)
    if request.method == "POST":
        activite.archive = True
        historique_activite = HistoriqueActivite()
        historique_activite.image = activite.image
        historique_activite.titre = activite.titre
        historique_activite.texte = activite.texte
        historique_activite.date = activite.date
        historique_activite.vues = activite.vues
        historique_activite.archive = True
        activite.save()
        historique_activite.save()
        data['form_is_valid'] = True
        activites = Activite.objects.filter(archive=False)
        data['activiteadmin'] = render_to_string('activiteadmin/listactiviteadmin.html',
                                                 {'activites': activites, 'historique_activite': historique_activite, })
    else:
        context = {
            'activite': activite,
        }
        data['html_form'] = render_to_string('activiteadmin/deleteactiviteadmin.html', context, request=request)

    return JsonResponse(data)


@login_required
def messageadmin(request):
    messages = Message.objects.filter(archive=False).order_by('-id')
    return render(request, 'messageadmin/messageadmin.html', locals())


@login_required
def deletemessageadmin(request, id):
    data = dict()
    message = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        d_form = DeleteMessage(request.POST, instance=message)
        if d_form.is_valid():
            message.save()
            data['form_is_valid'] = True
            messages = Contact.objects.filter(archive=False).order_by('lu')
            data['messageadmin'] = render_to_string('messageadmin/listmessageadmin.html',
                                                    {'messages': messages})
    else:
        d_form = DeleteMessage(instance=message)
        context = {
            'd_form': d_form,
            'message': message,
        }
        data['html_form'] = render_to_string('messageadmin/deletemessageadmin.html', context, request=request)

    return JsonResponse(data)


@login_required
def voirmessageclient(request, id):
    message = get_object_or_404(Contact, id=id)
    return render(request, 'messageadmin/voirmessageclient.html', locals())


@login_required
def updatebanniereaccueil(request):
    banniereaccueil = BanniereAccueil.objects.get(label="BanniereAccueil")
    notremission = NotreMission.objects.get(label="NotreMission")
    valeur = Valeur.objects.get(label="Valeur")
    productivite = Productivite.objects.get(label="Productivite")
    diamond = Diamond.objects.get(label="Diamond")
    financement = Financement.objects.get(label="Financement")
    expertise = Expertise.objects.get(label="Expertise")
    motdudg = MotDuDG.objects.get(label="MotDuDG")
    performance = Performance.objects.get(label="Performance")
    footer = Footer.objects.get(label="Footer")

    """ BanniereAccueil """

    if request.method == "POST":
        b_form = BanniereAccueilForm(request.POST, request.FILES, instance=banniereaccueil, prefix='banniere')
        nm_form = NotreMissionForm(request.POST, instance=notremission, prefix='notremission')
        v_form = ValeurForm(request.POST, instance=valeur, prefix='valeur')
        pr_form = ProductiviteForm(request.POST, instance=productivite, prefix='productivite')
        d_form = DiamondForm(request.POST, instance=diamond, prefix='diamond')
        fi_form = FinancementForm(request.POST, instance=financement, prefix='financement')
        e_form = ExpertiseForm(request.POST, instance=expertise, prefix='expertise')
        mdd_form = MotDuDGForm(request.POST, request.FILES, instance=motdudg, prefix='motdudg')
        p_form = PerformanceForm(request.POST, instance=performance, prefix='performance')
        f_form = FooterForm(request.POST, instance=footer, prefix='footer')

        if b_form.is_valid() and nm_form.is_valid() and v_form.is_valid() and pr_form.is_valid() and d_form.is_valid() \
                and fi_form.is_valid() and e_form.is_valid() and mdd_form.is_valid() and p_form.is_valid() \
                and f_form.is_valid():
            b_form.save()
            nm_form.save()
            v_form.save()
            pr_form.save()
            d_form.save()
            fi_form.save()
            e_form.save()
            mdd_form.save()
            p_form.save()
            f_form.save()
            return redirect('updatebanniereaccueil')

    else:
        b_form = BanniereAccueilForm(prefix='banniere', instance=banniereaccueil)
        nm_form = NotreMissionForm(prefix='notremission', instance=notremission)
        v_form = ValeurForm(prefix='valeur', instance=valeur)
        pr_form = ProductiviteForm(prefix='productivite', instance=productivite)
        d_form = DiamondForm(prefix='diamond', instance=diamond)
        fi_form = FinancementForm(prefix='financement', instance=financement)
        e_form = ExpertiseForm(prefix='expertise', instance=expertise)
        mdd_form = MotDuDGForm(prefix='motdudg', instance=motdudg)
        p_form = PerformanceForm(prefix='performance', instance=performance)
        f_form = FooterForm(prefix='footer', instance=footer)

    return render(request, 'parametre/accueil.html', locals())


def updateapropos(request):
    propos = Apropos.objects.get(label="Apropos")

    if request.method == "POST":
        a_form = AproposForm(request.POST, request.FILES, instance=propos)
        if a_form.is_valid():
            a_form.save()
            return redirect('updateapropos')
    else:
        a_form = AproposForm(instance=propos)

    return render(request, 'parametre/apropos.html', {'a_form': a_form})


def updatenossolutions(request):
    nossolutions = NosSolutions.objects.get(label="NosSolutions")

    if request.method == "POST":
        s_form = NosSolutionsForm(request.POST,
                                  request.FILES,
                                  instance=nossolutions)
        if s_form.is_valid():
            s_form.save()
            return redirect('updatenossolutions')
    else:
        s_form = NosSolutionsForm(instance=nossolutions)

    return render(request, 'parametre/nossolutions.html', {'s_form': s_form})
