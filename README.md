# Desafio de Desenvolvimento — Python

Solução das três questões propostas no desafio técnico.

## Requisitos
- Python 3.10 ou superior
- Nenhuma biblioteca externa

## Questão 1 — Comissão de vendas
Lê `data/vendas.json` e calcula a comissão venda a venda:
- valor < R$ 100,00: 0%
- R$ 100,00 <= valor < R$ 500,00: 1%
- valor >= R$ 500,00: 5%

Execute:
```bash
python questao_1_comissoes.py
```

## Questão 2 — Movimentação de estoque
Permite entrada ou saída dos produtos existentes em `data/estoque.json`.
Cada operação recebe um UUID único, descrição, tipo e quantidade. Saídas que deixariam o estoque negativo são rejeitadas. O novo saldo é persistido no JSON.

Execute:
```bash
python questao_2_estoque.py
```

## Questão 3 — Juros por atraso
Recebe um valor e uma data de vencimento. Se houver atraso, aplica juros simples de 2,5% por dia:

`juros = valor × 0,025 × dias_em_atraso`

Se o vencimento for hoje ou uma data futura, os juros são zero.

Execute:
```bash
python questao_3_juros.py
```

## Decisões técnicas
- `Decimal` é utilizado para cálculos monetários, evitando imprecisões típicas de `float`.
- `pathlib` torna o acesso aos JSON independente do diretório de execução.
- UUID identifica cada movimentação de estoque de forma única.
- As regras de negócio foram isoladas em funções para facilitar manutenção e testes.
