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
    return render(request, 'formation/formule.html', locals())


def calendrier(request):
    return render(request, 'formation/calendrier.html', locals())


def calendrier2(request):
    return render(request, 'formation/calendrier2.html', locals())
