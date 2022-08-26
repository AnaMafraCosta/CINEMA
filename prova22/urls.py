"""prova22 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from prova02.views import teste1, create_sala, lista_sala, atualizar_sala, deletar_sala

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testes/', teste1),
    path('listasala/', lista_sala, name="listasala"),
    path('sala/', create_sala, name= "url_criar_sala"),
    path('atualizarsala/<int:id_sala>', atualizar_sala, name= "url_atualizar_sala"),
    path('deletarsala/<int:id_sala>', deletar_sala, name= "url_deletar_sala"),
]
