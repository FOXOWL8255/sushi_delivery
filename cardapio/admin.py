from django.contrib import admin

# importamos as tabelas que eu criei em models.py
from .models import Categoria, Produto

#registramos as duas tabelas para aparecerem no painel 
admin.site.register(Categoria)
admin.site.register(Produto)
