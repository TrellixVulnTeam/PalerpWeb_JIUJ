"""Web1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from apps.productos.views import tienda_view, prueba
from apps.general.views import index_view, nosotros_view, contactanos_view, productos_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tienda/$', tienda_view, name = 'tienda'),
    url(r'^$', index_view, name = 'index'),
    url(r'^nosotros/$', nosotros_view, name = 'nosotros'),
    url(r'^productos/$', productos_view, name = 'productos'),
    url(r'^contactanos/$', contactanos_view, name = 'contactanos'),
    url(r'^test/', prueba, name = 'prueba'),
]
