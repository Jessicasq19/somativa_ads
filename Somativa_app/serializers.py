from rest_framework import serializers
from .models import *

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Clientes
        fields = '__all__'

class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Servicos
        fields = '__all__'

class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Funcionarios
        fields = '__all__'

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Produtos
        fields = '__all__'

class AutosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Autos
        fields = '__all__'

class ManutencoesSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Manutencoes
        fields = '__all__'

class PagamentosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Pagamentos
        fields = '__all__'

class ItensManutSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = ItensManut
        fields = '__all__'