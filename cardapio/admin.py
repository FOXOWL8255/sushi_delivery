from django.contrib import admin

#importamos as 3 tabelas que criamos 
from .models import Categoria, Produto, ImagemProduto

# REGISTRAR A categoria para podermos adiciomar ( temakis, bebidas, etc)
admin.site.register(Categoria)

#Essa classe cria um "bloco" de imagens extras para colocar dentro do produt 
class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 5 #quantos campos vazios vão aparecer

#essa classe configura a página de cadastro do Produto no painel 
class ProdutoAdmin(admin.ModelAdmin):
    # Avisa para incluir aquele "bloco" de imagens lá no final da página do produto
    inlines = [ImagemProdutoInline]

# Registramos o Produto usando a nossa configuração personalizada (ProdutoAdmin)
admin.site.register(Produto, ProdutoAdmin)