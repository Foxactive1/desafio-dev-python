from __future__ import annotations

import json
from pathlib import Path
from uuid import uuid4

ARQUIVO_ESTOQUE = Path(__file__).parent / "data" / "estoque.json"


def carregar_estoque(caminho: Path = ARQUIVO_ESTOQUE) -> dict:
    with caminho.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_estoque(dados: dict, caminho: Path = ARQUIVO_ESTOQUE) -> None:
    with caminho.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)


def buscar_produto(dados: dict, codigo: int) -> dict:
    for produto in dados["estoque"]:
        if produto["codigoProduto"] == codigo:
            return produto
    raise ValueError("Produto não encontrado.")


def movimentar_estoque(
    codigo_produto: int,
    tipo: str,
    quantidade: int,
    descricao_movimentacao: str,
    caminho: Path = ARQUIVO_ESTOQUE,
) -> dict:
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")

    tipo = tipo.strip().lower()
    if tipo not in {"entrada", "saida"}:
        raise ValueError("Tipo de movimentação deve ser 'entrada' ou 'saida'.")

    if not descricao_movimentacao.strip():
        raise ValueError("A descrição da movimentação é obrigatória.")

    dados = carregar_estoque(caminho)
    produto = buscar_produto(dados, codigo_produto)
    estoque_anterior = produto["estoque"]

    if tipo == "entrada":
        produto["estoque"] += quantidade
    else:
        if quantidade > produto["estoque"]:
            raise ValueError("Saída não permitida: estoque insuficiente.")
        produto["estoque"] -= quantidade

    salvar_estoque(dados, caminho)

    return {
        "idMovimentacao": str(uuid4()),
        "descricaoMovimentacao": descricao_movimentacao.strip(),
        "tipo": tipo,
        "codigoProduto": produto["codigoProduto"],
        "descricaoProduto": produto["descricaoProduto"],
        "quantidade": quantidade,
        "estoqueAnterior": estoque_anterior,
        "estoqueFinal": produto["estoque"],
    }


def main() -> None:
    print("MOVIMENTAÇÃO DE ESTOQUE")
    print("-" * 40)

    try:
        codigo = int(input("Código do produto: "))
        tipo = input("Tipo [entrada/saida]: ")
        quantidade = int(input("Quantidade: "))
        descricao = input("Descrição da movimentação: ")

        resultado = movimentar_estoque(codigo, tipo, quantidade, descricao)

        print("\nMovimentação realizada com sucesso.")
        print(f"ID: {resultado['idMovimentacao']}")
        print(f"Produto: {resultado['descricaoProduto']}")
        print(f"Estoque anterior: {resultado['estoqueAnterior']}")
        print(f"Estoque final: {resultado['estoqueFinal']}")
    except (ValueError, OSError, json.JSONDecodeError) as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
