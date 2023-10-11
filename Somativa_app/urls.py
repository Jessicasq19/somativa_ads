from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'clientes',ClientesView)
router.register(r'servicos',ServicosView)
router.register(r'funcionarios',FuncionariosView)
router.register(r'produtos',ProdutosView)
router.register(r'autos',AutosView)
router.register(r'manutencoes',ManutencoesView)
router.register(r'pagamentos',PagamentosView)
router.register(r'itens manutenção',ItensManutView)


urlpatterns = router.urls
