from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP

TAXA_DIARIA = Decimal("0.025")


def calcular_juros(
    valor: Decimal,
    vencimento: date,
    data_atual: date | None = None,
) -> tuple[int, Decimal, Decimal]:
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")

    hoje = data_atual or date.today()
    dias_atraso = max((hoje - vencimento).days, 0)
    juros = valor * TAXA_DIARIA * dias_atraso
    juros = juros.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    total = (valor + juros).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return dias_atraso, juros, total


def moeda(valor: Decimal) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main() -> None:
    print("CÁLCULO DE JUROS POR ATRASO")
    print("-" * 40)

    try:
        valor = Decimal(input("Valor (ex.: 1000.00): ").replace(",", "."))
        texto_data = input("Data de vencimento [dd/mm/aaaa]: ")
        vencimento = datetime.strptime(texto_data, "%d/%m/%Y").date()

        dias, juros, total = calcular_juros(valor, vencimento)

        print(f"\nDias em atraso: {dias}")
        print(f"Juros: {moeda(juros)}")
        print(f"Valor atualizado: {moeda(total)}")
    except (ValueError, ArithmeticError) as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
