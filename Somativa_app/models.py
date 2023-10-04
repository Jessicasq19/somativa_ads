from django.db import models
from django.utils import timezone

# Create your models here.

class Clientes(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    telefone = models.PositiveIntegerField()
    email = models.CharField(max_length=150)
    rua = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    cidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Servicos(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=20, decimal_places=2)


    def __str__(self):
        return self.nome
    

class Funcionarios(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    telefone = models.PositiveIntegerField()
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
    

class Produtos(models.Model):
    nome = models.CharField(max_length=150)
    qtde = models.IntegerField()
    codigo = models.CharField(max_length=13)
    fabricante = models.CharField(max_length=150)
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    

class Autos(models.Model):

    tipos = [
        ("moto", "Moto"),
        ("carro", "Carro"),
        ("caminhao", "Caminhão"),
        ("outros", "Outros")
    ]

    nome = models.CharField(max_length=150)
    tipos = models.CharField(max_length=8, choices=tipos)
    marca = models.CharField(max_length=20, null=True)
    modelo = models.CharField(max_length=50, null=True)
    ano = models.IntegerField(null=True)

    def __str__(self):
        return self.nome

