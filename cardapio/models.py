from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):

    # Charfield é usado para textos curtos e é obrigatório 
    nome = models.CharField(max_length=150)

    # TextField é para textos longos (como lista de peças ou combos)
    descricao = models.TextField(blank=True, null=True)

    # DecimalField é o formato perfeito para trabalhar com dinheiro
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    # ForeignKey (tabela estrangeira) é o que conecta tabelas diferentes 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # imagefield gerencia o upload de fotos (alinhado corretamente!)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)

    # A função __str__ muda o nome de exibição no painel administrativo
    def __str__(self):
        return self.nome

# Essa nova tabela vai guardar fotos extras dos produtos 
class ImagemProduto(models.Model):
    # Conecta essa imagem a um produto especifico. 
    # O related_name='imagens' é o que vai nos permitir criar o carrossel depois!
    produto = models.ForeignKey(Produto, related_name='imagens', on_delete=models.CASCADE)
    
    # Campo que faz o upload da foto extra
    imagem = models.ImageField(upload_to='produtos/galeria/')

    def __str__(self):
        return f"Foto extra de {self.produto.nome}"