from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from cabinet.forms import ContactForm, ArticleForm, ActiviteForm
from cabinet.models import Article, Activite


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
    return render(request, 'solution/solution.html', locals())


def activite(request):
    actvites = Activite.objects.filter(archive=False)

    context = {
        'activites': actvites,
    }
    return render(request, 'activite/activite.html', context)


def article(request):
    articles = Article.objects.filter(archive=False)

    context = {
        "articles": articles
    }
    return render(request, 'article/article.html', context)


def apropos(request):
    return render(request, 'apropos/apropos.html', locals())


def contacteznous(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacteznous')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contacteznous/contacteznous.html', context)


def feedback(request):
    return render(request, 'feedback/feedback.html', locals())


def dashboard(request):
    return render(request, 'dashboard.html', locals())


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


def deleteactiviteadmin(request, id):
    data = dict()
    activite = get_object_or_404(Activite, id=id)
    if request.method == "POST":
        activite.archive = True
        activite.save()
        data['form_is_valid'] = True
        activites = Activite.objects.filter(archive=False)
        data['activiteadmin'] = render_to_string('activiteadmin/listactiviteadmin.html',
                                                            {'activites': activites})
    else:
        context = {
            'activite': activite,
        }
        data['html_form'] = render_to_string('activiteadmin/deleteactiviteadmin.html', context, request=request)

    return JsonResponse(data)
