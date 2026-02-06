"""
Sistema de Clientes
Projeto para portfólio - Desenvolvido em Python
Permite cadastrar, listar e deletar clientes usando JSON como banco de dados
"""

import json

ARQUIVO = "clientes.json"


def carregar_clientes():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []


def salvar_clientes(clientes):
    with open(ARQUIVO, "w") as f:
        json.dump(clientes, f, indent=4)


def cadastrar_cliente():
    clientes = carregar_clientes()

    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")

    clientes.append({
        "nome": nome,
        "idade": idade,
        "email": email
    })

    salvar_clientes(clientes)
    print("✅ Cliente cadastrado!\n")


def listar_clientes():
    clientes = carregar_clientes()

    if not clientes:
        print("Nenhum cliente cadastrado.\n")
        return

    for i, c in enumerate(clientes, start=1):
        print(f"{i} - {c['nome']} | {c['idade']} anos | {c['email']}")
    print()


def deletar_cliente():
    clientes = carregar_clientes()
    listar_clientes()

    indice = int(input("Número do cliente: ")) - 1

    if 0 <= indice < len(clientes):
        clientes.pop(indice)
        salvar_clientes(clientes)
        print("🗑 Cliente removido!\n")
    else:
        print("Cliente inválido.\n")


def menu():
    while True:
        print("==== SISTEMA DE CLIENTES ====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Deletar")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            deletar_cliente()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.\n")


menu()
