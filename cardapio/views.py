from django.shortcuts import render, get_object_or_404

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


# Essa é a função que vai carregar a página de detalhes de um produto específico
def detalhe_produto(request, produto_id):
    
    # Busca o produto pelo ID no banco ou retorna uma página 404 se não existir
    produto = get_object_or_404(Produto, id=produto_id)

    # Empacota o produto individual em um dicionário para enviar ao HTML
    context = {
        'produto': produto
    }

    # Renderiza a página de detalhes entregando o produto selecionado
    return render(request, 'cardapio/detalhe_produto.html', context)