from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Filme
from .models import Sala
from .form import SalaForm


# Create your views here.
def teste1(request):
    return render(request, "teste.html")

#def listagem(request):
#    filmes = Filme.objects.all()
#    pacote = {"filme_chave": filmes}
#    return render(request, "lista.html", pacote)

def lista_sala(request):
    salas = Sala.objects.all()
    pacote = {"sala_chave": salas}
    return render(request, "listasala.html", pacote)

def create_sala(request):
    form = SalaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("listasala")

    pacote = {"form_sala": form}
    return render(request, "sala.html", pacote)

def atualizar_sala(request, id_sala):
    sala = Sala.objects.get(pk=id_sala)
    
    form = SalaForm(request.POST or None, instance=sala)
    if form.is_valid():
        form.save()
        return redirect("listasala")

    pacote = {"form_sala": form}
    return render(request, "sala.html", pacote)

def deletar_sala(request, id_sala):
    sala = Sala.objects.get(pk=id_sala)
    sala.delete()

    return redirect("listasala")