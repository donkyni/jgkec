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

from cabinet.views import acceuil, contacts, expertise, ingenierie, management, finance, developpement, insertion, \
    formation, formule, calendrier, calendrier2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', acceuil, name="acceuil"),
    path('contacts/', contacts, name="contacts"),
    path('expertise/', expertise, name="expertise"),
    path('ingenierie/', ingenierie, name="ingenierie"),
    path('management/', management, name="management"),
    path('finance/', finance, name="finance"),
    path('developpement', developpement, name="developpement"),
    path('insertion/', insertion, name="insertion"),
    path('formation/', formation, name="formation"),
    path('formule/', formule, name="formule"),
    path('calendrier/', calendrier, name="calendrier"),
    path('calendrier2/', calendrier2, name="calendrier2"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
