from django.shortcuts import render
from galeria.models import Fotografia

def index(request):
    fotografia = Fotografia.objects.all()
    return render(request, 'galeria/index.html', { 'cards': fotografia})

def imagem(request):
    return render(request, 'galeria/imagem.html')
