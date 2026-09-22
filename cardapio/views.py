from django.shortcuts import render, get_object_or_404

# Importamos a Categoria junto com o Produto
from .models import Produto, Categoria 

def vitrine_digital(request):
    # Pega todas as categorias no banco para criar os botões
    categorias = Categoria.objects.all()
    
    # Verifica se tem algum filtro na URL (ex: ?categoria=1)
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        produtos = Produto.objects.filter(categoria_id=categoria_id)
    else:
        produtos = Produto.objects.all()
        
    # O segredo está aqui: enviamos as categorias para o HTML!
    contexto = {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_ativa': categoria_id
    }
    return render(request, 'cardapio/vitrine.html', contexto)

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'cardapio/detalhe_produto.html', {'produto': produto})