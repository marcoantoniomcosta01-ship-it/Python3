from django.shortcuts import render
from ecommerce.serializers import ProdutoSerializer, CategoriaSerializer
from ecommerce.models import Produto, Categoria
from rest_framework import viewsets
# Create your views here.

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer  