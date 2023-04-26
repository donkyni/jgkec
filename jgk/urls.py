"""jgk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.urls import re_path as url

from cabinet import views

from cabinet.views import acceuil, contacts, expertise, ingenierie, management, finance, insertion, \
    formation, formule, calendrier, calendrier2, sondage, reprise, etude, solution, activite, article, \
    apropos, contacteznous, feedback, dashboard, articleadmin, activiteadmin, messageadmin, login_url, logout_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', acceuil, name="acceuil"),
    path('contacts/', contacts, name="contacts"),
    path('expertise/', expertise, name="expertise"),
    path('ingenierie/', ingenierie, name="ingenierie"),
    path('management/', management, name="management"),
    path('finance/', finance, name="finance"),
    path('reprise/', reprise, name="reprise"),
    path('etude', etude, name="etude"),
    path('insertion/', insertion, name="insertion"),
    path('formation/', formation, name="formation"),
    path('formule/', formule, name="formule"),
    path('calendrier/', calendrier, name="calendrier"),
    path('calendrier2/', calendrier2, name="calendrier2"),
    path('sondage/', sondage, name="sondage"),
    path('solution/', solution, name="solution"),
    path('activite/', activite, name="activite"),
    path('article/', article, name="article"),
    path('apropos/', apropos, name="apropos"),
    path('contacteznous/', contacteznous, name="contacteznous"),
    path('feedback/', feedback, name="feedback"),
    # ADMIN URLs
    path('login_url/', login_url, name="login_url"),
    path('logout_url/', logout_url, name="logout_url"),
    path('dashboard/', dashboard, name="dashboard"),
    path('articleadmin/', articleadmin, name="articleadmin"),
    path(r'^(?P<id>\d+)/modifier-un-article', views.updatearticleadmin, name="updatearticleadmin"),
    path(r'^(?P<id>\d+)/supprimer-un-article', views.deletearticleadmin, name="deletearticleadmin"),
    path('activiteadmin/', activiteadmin, name="activiteadmin"),
    path(r'^(?P<id>\d+)/modifier-une-activite', views.updateactiviteadmin, name="updateactiviteadmin"),
    path(r'^(?P<id>\d+)/supprimer-une-activite', views.deleteactiviteadmin, name="deleteactiviteadmin"),
    path('messageadmin/', messageadmin, name="messageadmin"),
    path(r'^(?P<id>\d+)/supprimer-un-message', views.deletemessageadmin, name="deletemessageadmin"),
    path(r'^(?P<id>\d+)/consulter-le-message', views.voirmessageclient, name="voirmessageclient"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
