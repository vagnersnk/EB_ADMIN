from django.contrib import admin
from .models import Estoque, Categoria, Fornecedor, Produto, Entrada

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_estoque', 'tipo')
    search_fields = ('nome_estoque',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria', 'ncm')
    search_fields = ('nome_categoria', 'ncm')

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_fornecedor', 'contato')
    search_fields = ('nome_fornecedor',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'fabricante', 'status')
    search_fields = ('nome_produto', 'fabricante')
    list_filter = ('status',)

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    # Aqui mostra os campos
    list_display = ('id', 'data_entrada', 'produto', 'fornecedor', 'estoque','quantidade')
    search_fields = ('produto__nome_produto', 'fornecedor__nome_fornecedor')
    list_filter = ('data_entrada',)
    date_hierarchy = 'data_entrada'