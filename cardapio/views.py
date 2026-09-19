from django.shortcuts import render

# É necessário importar as tabelas para a view acessar o banco de dados 
from .models import Produto

# Essa é a função que vai carregar a página do cardápio p/ Cliente
def vitrine_digital(request):
    
    # comando que pesca todos os produtos do banco de dados 
    produtos_do_banco = Produto.objects.all()

    # transformamos os produtos em um dicionário para enviar ao HTML 
    context = {
        'produtos': produtos_do_banco
    }

    # renderizar a vitrine.html entregando a ela o pacote de dados 
    return render(request, 'cardapio/vitrine.html', context)