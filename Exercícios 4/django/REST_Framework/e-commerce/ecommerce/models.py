from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    descricao = models.TextField(max_length=500)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome