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
    qtde_estoque = models.IntegerField()
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

class Manutencoes(models.Model):
    autoID = models.ForeignKey(Autos, related_name='autoFk', on_delete=models.CASCADE)
    funcionarioID = models.ForeignKey(Funcionarios, related_name='funcFk', on_delete=models.CASCADE)

    def __str__(self):
        return self.autoID
    
    
class Pagamentos(models.Model):
    TipoPag = [
        ("pix", "PIX"),
        ("credito", "CRÉDITO"),
        ("debito", "DÉBITO"),
        ("dinheiro", "DINHEIRO"),
        ("outros", "OUTROS"),
    ]

    Status = [
        ("pendente", "PENDENTE!"),
        ("aprovado", "APROVADO!"),
        ("nao autorizado", "NÃO AUTORIZADO!"),
    ]
    manutencaoID = models.ForeignKey(Manutencoes, related_name='manut', on_delete=models.CASCADE)
    desconto = models.DecimalField(max_digits=5, decimal_places=2)
    valorFinal = models.DecimalField(max_digits=5, decimal_places=2)
    tipoPag = models.CharField(max_length=50, choices=TipoPag, null=True)
    status = models.CharField(max_length=50, choices=Status, null=True)

    def __str__(self):
        return self.manutencaoID
    

class ItensManut(models.Model):
    manutencoesID = models.ForeignKey(Manutencoes, related_name='manutFk', on_delete=models.CASCADE)
    produtoID = models.ForeignKey(Produtos, related_name='prodFk', on_delete=models.CASCADE)
    qtde_usada = models.IntegerField()
    servicoID = models.ForeignKey(Servicos, related_name='servFk', on_delete=models.CASCADE)

    def __str__(self):
        return self.manutencaoID