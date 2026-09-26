from django.urls import path
from . import views

urlpatterns = [
    path('', views.vitrine_digital, name='vitrine'),
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    
    # Nova rota para esvaziar o carrinho
    path('limpar/', views.limpar_carrinho, name='limpar_carrinho'),
]