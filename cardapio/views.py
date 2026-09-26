# 1. Adicionamos o 'redirect' aqui em cima
from django.shortcuts import render, get_object_or_404, redirect

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

# --- AQUI COMEÇA O NOSSO NOVO CÓDIGO ---

def adicionar_ao_carrinho(request, produto_id):
    # Busca o sushi específico no qual o cliente clicou
    produto = get_object_or_404(Produto, id=produto_id)
    
    # Pega o "bloco de notas" (carrinho) do cliente. Se estiver vazio, cria um novo {}
    carrinho = request.session.get('carrinho', {})
    
    # O bloco de notas do Django exige que o ID do produto seja um texto (string)
    id_str = str(produto_id)
    
    # Verifica se o sushi já está anotado lá. Se estiver, só aumenta a quantidade.
    if id_str in carrinho:
        carrinho[id_str]['quantidade'] += 1
    else:
        # Se for o primeiro clique neste sushi, anota o nome, preço e quantidade 1
        carrinho[id_str] = {
            'nome': produto.nome,
            'preco': str(produto.preco), 
            'quantidade': 1
        }
        
    # Guarda o bloco de notas atualizado de volta na memória do navegador
    request.session['carrinho'] = carrinho
    
    # Manda o cliente de volta para a vitrine para continuar a comprar
    return redirect('vitrine')