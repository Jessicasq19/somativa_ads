from django.contrib import admin
from .models import *

# Register your models here.

class detClientes(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id",)
    search_fields = ("nome",)
    list_per_page = 5

admin.site.register(Clientes, detClientes)


class detServicos(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id",)
    search_fields = ("nome",)
    list_per_page = 5

admin.site.register(Servicos, detServicos)


class detFuncionarios(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id",)
    search_fields = ("nome",)
    list_per_page = 5

admin.site.register(Funcionarios, detFuncionarios)


class detProdutos(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id",)
    search_fields = ("nome",)
    list_per_page = 5

admin.site.register(Produtos, detProdutos)


class detAutos(admin.ModelAdmin):
    list_display = ("id", "nome")
    list_display_links = ("id",)
    search_fields = ("nome",)
    list_per_page = 5

admin.site.register(Autos, detAutos)


class detManutencoes(admin.ModelAdmin):
    list_display = ("id",)
    list_display_links = ("id",)
    search_fields = ("id",)
    list_per_page = 5

admin.site.register(Manutencoes, detManutencoes)


class detPagamentos(admin.ModelAdmin):
    list_display = ("id",)
    list_display_links = ("id",)
    search_fields = ("id",)
    list_per_page = 5

admin.site.register(Pagamentos, detPagamentos)


class detItensManut(admin.ModelAdmin):
    list_display = ("id",)
    list_display_links = ("id",)
    search_fields = ("id",)
    list_per_page = 5

admin.site.register(ItensManut, detItensManut)