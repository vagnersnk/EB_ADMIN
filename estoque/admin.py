from django.contrib import admin
from .models import Estoque, Fornecedor, Produto, Entrada
from django.contrib.admin import AdminSite

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_estoque', 'tipo')
    search_fields = ('nome_estoque',)



@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_fornecedor', 'contato')
    search_fields = ('nome_fornecedor',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_produto','estoque','validade','dias_restantes', 'fabricante', 'status','visto_por_ultimo')
    search_fields = ('nome_produto', 'fabricante')
    list_filter = ('status',)



@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    # Aqui mostra os campos
    list_display = ('id','produto','unidade_entrada','quantidade', 'data_entrada', 'fornecedor','validade')
    search_fields = ('produto__nome_produto', 'fornecedor__nome_fornecedor')
    list_filter = ('data_entrada',)
    date_hierarchy = 'data_entrada'
    exclude = ('unidade_entrada',)

    def save_model(self, request, obj, form, change):
        if obj.produto:
            obj.unidade_entrada = obj.produto.unidade_entrada  # Puxa do produto selecionado
        super().save_model(request, obj, form, change)




