from django.contrib import admin 
from django.urls import path

#1. imoportamos o arquivo de views do nosso aplicativo cardapio
from cardapio import views

urlpatterns = [
    #essa é a rota do painel administrtivo 
    path('admin/', admin.site.urls),
    
#2. criamos a rota da pag inicial do restaurante 
# as aspas vazias significam a pasta raiz do site 
# Quando o cliente acessar a raiz, o Django aciona a sua views.vitrine_digital
path('',views.vitrine_digital, name='vitrine'),
]

