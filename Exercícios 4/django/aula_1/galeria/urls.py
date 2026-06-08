from django.urls import path
from galeria.views import index, conteudo, login
urlpatterns = [
    path('', index, name='index'),
    path('conteudo/', conteudo, name='conteudo')
]