from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Categoria 

def vitrine_digital(request):
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        produtos = Produto.objects.filter(categoria_id=categoria_id)
    else:
        produtos = Produto.objects.all()
        
    carrinho = request.session.get('carrinho', {})
    total_itens = sum(item['quantidade'] for item in carrinho.values())
        
    contexto = {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_ativa': categoria_id,
        'total_itens': total_itens
    }
    return render(request, 'cardapio/vitrine.html', contexto)

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'cardapio/detalhe_produto.html', {'produto': produto})

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = request.session.get('carrinho', {})
    id_str = str(produto_id)
    
    if id_str in carrinho:
        carrinho[id_str]['quantidade'] += 1
    else:
        carrinho[id_str] = {
            'nome': produto.nome,
            'preco': str(produto.preco), 
            'quantidade': 1
        }
        
    request.session['carrinho'] = carrinho
    return redirect('vitrine')

def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    
    # Calcula o valor total do pedido
    total_pedido = sum(float(item['preco']) * item['quantidade'] for item in carrinho.values())
    
    contexto = {
        'carrinho': carrinho,
        'total_pedido': total_pedido
    }
    return render(request, 'cardapio/carrinho.html', contexto)


def limpar_carrinho(request):
    # Se o "bloco de notas" do carrinho existir na sessão, nós apagamo-lo
    if 'carrinho' in request.session:
        del request.session['carrinho']
    
    # Após limpar, redireciona o cliente de volta para a vitrine
    return redirect('vitrine')