import json
import os

ARQUIVO = "estoque.json"


def carregar_estoque():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_estoque(estoque):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(estoque, arquivo, indent=4, ensure_ascii=False)


def adicionar_produto(estoque):
    print("\n=== ADICIONAR PRODUTO ===")
    nome = input("Nome do produto: ").strip()

    if not nome:
        print("O nome não pode ficar vazio.")
        return

    try:
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: R$ ").replace(",", "."))
    except ValueError:
        print("Digite valores válidos.")
        return

    if quantidade < 0 or preco < 0:
        print("Quantidade e preço não podem ser negativos.")
        return

    estoque.append({
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    })

    salvar_estoque(estoque)
    print("Produto adicionado com sucesso.")


def listar_produtos(estoque):
    print("\n=== ESTOQUE ===")

    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    for i, produto in enumerate(estoque, start=1):
        total = produto["quantidade"] * produto["preco"]

        print(f"\n{i}. {produto['nome']}")
        print(f"   Quantidade: {produto['quantidade']}")
        print(f"   Preço: R$ {produto['preco']:.2f}")
        print(f"   Valor em estoque: R$ {total:.2f}")


def buscar_produto(estoque):
    print("\n=== BUSCAR PRODUTO ===")
    busca = input("Digite o nome do produto: ").strip().lower()

    encontrados = [
        produto for produto in estoque
        if busca in produto["nome"].lower()
    ]

    if not encontrados:
        print("Nenhum produto encontrado.")
        return

    for produto in encontrados:
        print(f"\nProduto: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R$ {produto['preco']:.2f}")


def alterar_quantidade(estoque):
    print("\n=== ALTERAR QUANTIDADE ===")
    nome = input("Nome do produto: ").strip().lower()

    for produto in estoque:
        if produto["nome"].lower() == nome:
            try:
                nova_quantidade = int(input("Nova quantidade: "))
            except ValueError:
                print("Digite uma quantidade válida.")
                return

            if nova_quantidade < 0:
                print("A quantidade não pode ser negativa.")
                return

            produto["quantidade"] = nova_quantidade
            salvar_estoque(estoque)
            print("Quantidade atualizada.")
            return

    print("Produto não encontrado.")


def remover_produto(estoque):
    print("\n=== REMOVER PRODUTO ===")
    nome = input("Nome do produto: ").strip().lower()

    for produto in estoque:
        if produto["nome"].lower() == nome:
            estoque.remove(produto)
            salvar_estoque(estoque)
            print("Produto removido com sucesso.")
            return

    print("Produto não encontrado.")


def mostrar_resumo(estoque):
    produtos = len(estoque)
    itens = sum(produto["quantidade"] for produto in estoque)
    valor = sum(produto["quantidade"] * produto["preco"] for produto in estoque)

    print("\n=== RESUMO ===")
    print(f"Produtos cadastrados: {produtos}")
    print(f"Itens no estoque: {itens}")
    print(f"Valor total: R$ {valor:.2f}")


def menu():
    estoque = carregar_estoque()

    while True:
        print("\n" + "=" * 35)
        print("       SISTEMA DE ESTOQUE")
        print("=" * 35)
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Alterar quantidade")
        print("5 - Remover produto")
        print("6 - Ver resumo")
        print("0 - Sair")
        print("=" * 35)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            buscar_produto(estoque)
        elif opcao == "4":
            alterar_quantidade(estoque)
        elif opcao == "5":
            remover_produto(estoque)
        elif opcao == "6":
            mostrar_resumo(estoque)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


menu()
