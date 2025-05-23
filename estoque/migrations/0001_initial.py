# Generated by Django 5.2 on 2025-04-19 17:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Estoque",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_estoque", models.CharField(max_length=100)),
                ("tipo", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Fornecedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_fornecedor", models.CharField(max_length=100)),
                ("contato", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_produto", models.CharField(max_length=100)),
                ("unidade_entrada", models.CharField(max_length=5)),
                ("fabricante", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[("A", "Ativo"), ("I", "Inativo")],
                        default="A",
                        max_length=1,
                    ),
                ),
                ("visto_por_ultimo", models.DateField(default=datetime.date.today)),
                ("validade", models.DateField(blank=True, null=True)),
                (
                    "estoque",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="estoque.estoque",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Entrada",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_entrada", models.DateField()),
                (
                    "unidade_entrada",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("quantidade", models.PositiveIntegerField()),
                (
                    "valor_unitario",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("validade", models.DateField(blank=True, null=True)),
                (
                    "fornecedor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="estoque.fornecedor",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="entradas_produto",
                        to="estoque.produto",
                    ),
                ),
            ],
        ),
    ]
