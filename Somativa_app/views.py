from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
#from .customFilters import *
from django.db.models import Avg
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from django.dispatch import receiver
from django.db.models.signals import post_save



class ClientesView(ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "id", "nome", "cpf", "telefone"

class ServicosView(ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "id", "nome", "preco"

class FuncionariosView(ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "id", "nome", "cpf", "telefone"

class ProdutosView(ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "id", "nome", "codigo", "preco_compra", "preco_venda"

class AutosView(ModelViewSet):
    queryset = Autos.objects.all()
    serializer_class = AutosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "id", "nome", "tipo", "marcas", "modelo", "ano"

class ManutencoesView(ModelViewSet):
    queryset = Manutencoes.objects.all()
    serializer_class = ManutencoesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "id", "autoID", "funcionarioID"

class PagamentosView(ModelViewSet):
    queryset = Pagamentos.objects.all()
    serializer_class = PagamentosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "id", "tipoPag", "status", "desconto", "valorFinal"

class ItensManutView(ModelViewSet):
    queryset = ItensManut.objects.all()
    serializer_class = ItensManutSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = "id", "manutencoesID", "produtoID", "servicoID"

    @receiver(post_save, sender=ItensManut)
    def update_qtde_produto(sender, instance, created, **kwargs):
        if created:
            produto= instance.produto
            produto.qtde_estoque -= instance.qtde_usada
            produto.save()

