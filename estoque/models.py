from django.db import models
import datetime
from django.core.exceptions import ValidationError


class Estoque(models.Model):
    nome_estoque = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_estoque



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
    visto_por_ultimo = models.DateField(default=datetime.date.today)
    validade = models.DateField(null=True, blank=True)
    estoque = models.ForeignKey(Estoque, on_delete=models.SET_NULL, null=True, blank=True)


    def dias_restantes(self):
        if self.validade:
            today = datetime.date.today()
            # Garantir que a validade não seja uma data no futuro
            if self.validade >= today:
                delta = self.validade - today  # Calcula a diferença de dias
                return delta.days
            else:
                return 0  # Retorna 0 se a validade já passou
        return None  # Retorna None se não houver validade

    dias_restantes.short_description = 'Dias Restantes'  # Agora fora da propriedade
    def __str__(self):
        return self.nome_produto


class Entrada(models.Model):
    data_entrada=models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True,related_name='entradas_produto')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    unidade_entrada = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True,related_name='entradas_unidade')
    quantidade = models.PositiveIntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    validade = models.DateField(null=True, blank=True)



    def __str__(self):
        return f"{self.data_entrada} - {self.produto}"



