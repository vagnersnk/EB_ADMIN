from django.db import models


class Estoque(models.Model):
    nome_estoque = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_estoque

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=100)
    ncm = models.CharField(max_length=8)
    def __str__(self):
        return self.nome_categoria

class Fornecedor(models.Model):
    nome_fornecedor= models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_fornecedor


class Produto(models.Model):
    class Status(models.TextChoices):
        ATIVO = 'A', 'Ativo'
        INATIVO = 'I', 'Inativo'
    nome_produto = models.CharField(max_length=100)
    unidade_entrada =models.CharField(max_length=5)
    fabricante = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.ATIVO)
    def __str__(self):
        return self.nome_produto


class Entrada(models.Model):
    data_entrada=models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    categoria= models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    estoque =models.ForeignKey(Estoque, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    validade = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.data_entrada} - {self.produto}"



