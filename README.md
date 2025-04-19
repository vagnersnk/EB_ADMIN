# EBADMIN Sistema basico de gerenciamento de estoque
## Descrição das Tabelas

### 1. Tabela ESTOQUE
- **id**: Chave primária (auto-incremento)
- **nome_estoque**: Nome do estoque (max 100 caracteres)
- **tipo**: Tipo de estoque (max 50 caracteres)

### 2. Tabela FORNECEDOR
- **id**: Chave primária (auto-incremento)
- **nome_fornecedor**: Nome do fornecedor (max 100 caracteres)
- **contato**: Informações de contato (max 100 caracteres)

### 3. Tabela PRODUTO
- **id**: Chave primária (auto-incremento)
- **nome_produto**: Nome do produto (max 100 caracteres)
- **unidade_entrada**: Unidade de medida (max 5 caracteres)
- **fabricante**: Nome do fabricante (max 100 caracteres)
- **status**: Estado do produto (A=Ativo, I=Inativo)
- **visto_por_ultimo**: Data do último registro
- **validade**: Data de validade (opcional)
- **estoque_id**: Chave estrangeira para ESTOQUE (opcional)

### 4. Tabela ENTRADA
- **id**: Chave primária (auto-incremento)
- **data_entrada**: Data de entrada do produto
- **produto_id**: Chave estrangeira para PRODUTO (opcional)
- **fornecedor_id**: Chave estrangeira para FORNECEDOR (opcional)
- **unidade_entrada**: Unidade de medida (max 5 caracteres)
- **quantidade**: Quantidade entrada (número positivo)
- **valor_unitario**: Valor por unidade (decimal)
- **validade**: Data de validade específica (opcional)

## Relacionamentos

1. Um **ESTOQUE** pode conter vários **PRODUTOS** (1:N)
2. Um **FORNECEDOR** pode estar associado a várias **ENTRADAS** (1:N)
3. Um **PRODUTO** pode ter várias **ENTRADAS** registradas (1:N)
