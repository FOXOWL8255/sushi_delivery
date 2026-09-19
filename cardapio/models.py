from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    # A classe Produto vai ser a nossa tabela de itens
    # do cardápio do banco de dados
class Produto(models.Model):

#Charfield é usado para textos curtos e é obrigatório 
#max_length=150 impõe um limite de 150 caracteres 

    nome = models.CharField(max_length=150)

#Textfiekd é para textos longos ( como lista de peças ou combos)
#blank=True e null = True avisam o banco de dados que é 
#opcional preencher o dado 

    descricao = models.TextField(blank=True, null=True)

#decimalField é o formato perfeito para trabalhar com dinheiro
#max_digits= diz que o valor pode ter até 8 numeros no total.
#decimal_places =2 garante que os últimos dois números sejam cents.

    preco = models.DecimalField(max_digits=8, decimal_places=2)

#Foreignkey ( tabela estrangeira ) é o que conecta tabelas diferentes 
# django interpreta : "Esse produto pertence à classe Categoria lá de cima".
#CASCADE: se o dono apagar a ctegoria "bebidas", todos os refrigerantes 
#são apagados juntos 

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

# A função __str__ muda o nome de exibição no painel administrativo do django 
#sem ela o django chamaria o item de "Produto object 1"
#com ela exibe o nome real (ex: combinado hot, "temaki cru ")

    def __str__ (self ):
        return self.nome   