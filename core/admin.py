from django.contrib import admin
from .models import Produto , Produto3


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo',)

@admin.register(Produto3)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'preco','estoque', 'slug', 'criado', 'modificado', 'ativo', )

