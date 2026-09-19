from django.urls import path
from . import views

# Rotas exclusivas do aplicativo cardapio
urlpatterns = [
    # Rota da página inicial (vitrine do restaurante)
    path('', views.vitrine_digital, name='vitrine'),
    
    # Rota dinâmica para a página de detalhes de cada produto usando o ID único
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe_produto'),
]