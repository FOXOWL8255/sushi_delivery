from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Categoria 
import urllib.parse # <-- IMPORTANTE: Necessário para formatar o texto para o WhatsApp

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
    total_pedido = sum(float(item['preco']) * item['quantidade'] for item in carrinho.values())
    
    # --- NOVO: MONTAGEM DA MENSAGEM DO WHATSAPP ---
    mensagem = "*Novo Pedido - Cardápio Digital* 🍣\n\n"
    for id_produto, item in carrinho.items():
        mensagem += f"- {item['quantidade']}x {item['nome']} (R$ {item['preco']})\n"
    mensagem += f"\n*Total do Pedido: R$ {total_pedido:.2f}*"
    
    # Substitua o número abaixo pelo número do WhatsApp do seu restaurante (Código do país + DDD + Número)
    # Exemplo para o Brasil (DDD 11): 5511999999999
    numero_whatsapp = "5561994446204" 
    
    # Converte o texto para formato de link seguro da internet
    mensagem_codificada = urllib.parse.quote(mensagem)
    whatsapp_url = f"https://wa.me/{numero_whatsapp}?text={mensagem_codificada}"
    # ----------------------------------------------
    
    contexto = {
        'carrinho': carrinho,
        'total_pedido': total_pedido,
        'whatsapp_url': whatsapp_url # Enviamos o link gerado para o HTML
    }
    return render(request, 'cardapio/carrinho.html', contexto)

def limpar_carrinho(request):
    if 'carrinho' in request.session:
        del request.session['carrinho']
    return redirect('vitrine')