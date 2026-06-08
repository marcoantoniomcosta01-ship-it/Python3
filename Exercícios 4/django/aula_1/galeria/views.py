from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def conteudo(request):
    return render(request, "conteudo.html")
