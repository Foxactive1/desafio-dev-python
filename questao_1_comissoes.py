from __future__ import annotations

import json
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ARQUIVO_VENDAS = Path(__file__).parent / "data" / "vendas.json"


def calcular_comissao(valor: Decimal) -> Decimal:
    if valor < Decimal("100"):
        return Decimal("0")
    if valor < Decimal("500"):
        return valor * Decimal("0.01")
    return valor * Decimal("0.05")


def carregar_vendas(caminho: Path = ARQUIVO_VENDAS) -> list[dict]:
    with caminho.open("r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados["vendas"]


def calcular_comissoes(vendas: list[dict]) -> dict[str, Decimal]:
    totais: dict[str, Decimal] = defaultdict(Decimal)

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = Decimal(str(venda["valor"]))
        totais[vendedor] += calcular_comissao(valor)

    return dict(totais)


def moeda(valor: Decimal) -> str:
    valor = valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main() -> None:
    vendas = carregar_vendas()
    comissoes = calcular_comissoes(vendas)

    print("COMISSÃO POR VENDEDOR")
    print("-" * 40)
    for vendedor, comissao in comissoes.items():
        print(f"{vendedor:<25} {moeda(comissao)}")


if __name__ == "__main__":
    main()
