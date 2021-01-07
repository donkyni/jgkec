from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


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


def developpement(request):
    return render(request, 'expertise/developpement.html', locals())


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
