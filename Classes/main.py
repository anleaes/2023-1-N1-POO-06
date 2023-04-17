import os
from typing import List
from cliente import Cliente
from filme import Filme
from sessao import Sessao

# Criação de objetos Filme, Sessao e Cliente
filmes = {
    "O Poderoso Chefão": Filme("O Poderoso Chefão", "2h 58min", "Drama", "16 anos"),
    "Toy Story": Filme("Toy Story", "1h 21min", "Animação", "Livre"),
    "Os Vingadores": Filme("Os Vingadores", "2h 23min", "Ação", "12 anos")
}

sessoes = [
    Sessao(filmes["O Poderoso Chefão"], "18h", 20.0, 100, 0, []),
    Sessao(filmes["O Poderoso Chefão"], "21h", 25.0, 50, 0, []),
    Sessao(filmes["Toy Story"], "14h", 15.0, 80, 0, [])
]

clientes = [
    Cliente("João", "123.456.789-00", "(11) 99999-9999",
            50.0, "1111 2222 3333 4444", 25),
    Cliente("Maria", "987.654.321-00", "(11) 88888-8888",
            100.0, "5555 6666 7777 8888", 30),
    Cliente("Roberta", "432.632.734-42", "(51) 98644-5732",
            60.00, "7384 6127 8743 6532", 23)
]


def listar_sessoes(sessoes: List[Sessao]):
    print("Sessões disponíveis:")
    for i, sessao in enumerate(sessoes):
        print(f"{i+1}. {sessao.filme.nome} - Horário: {sessao.horario} - Preço: R${sessao.preco:.2f} - Ingressos disponíveis: {sessao.ingressos_disponiveis}")


def selecionar_sessao(sessoes: List[Sessao]) -> Sessao:
    listar_sessoes(sessoes)
    while True:
        try:
            sessao_opcao = int(input("Selecione a sessão desejada: "))
            if 1 <= sessao_opcao <= len(sessoes) and sessoes[sessao_opcao-1].ingressos_disponiveis > 0:
                return sessoes[sessao_opcao - 1]
            else:
                raise ValueError
        except (ValueError, IndexError):
            print("Opção inválida ou sessão sem ingressos disponíveis.")


def comprar_ingressos(sessao: Sessao, cliente: Cliente):
    while True:
        qtd_ingressos = input("Quantos ingressos deseja comprar? ")
        if qtd_ingressos.isdigit() and int(qtd_ingressos) > 0:
            break
        else:
            print("Valor inválido. Digite um número inteiro positivo.")
    cliente.comprar_ingresso(sessao, int(qtd_ingressos))


def adicionar_saldo(cliente: Cliente):
    while True:
        saldo = input("Digite o valor que deseja adicionar ao seu saldo: R$")
        if saldo.replace(".", "", 1).isdigit() and float(saldo) >= 0:
            cliente.adicionar_saldo(float(saldo))
            break
        else:
            print("Valor inválido. Digite um número positivo.")


def ver_sessoes(sessoes: List[Sessao]):
    os.system('cls' if os.name == 'nt' else 'clear')
    listar_sessoes(sessoes)


def ver_saldo(cliente: Cliente):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Seu saldo atual é de R${cliente.saldo:.2f}")


def menu_cliente(cliente: Cliente):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Bem-vindo {cliente.nome}!")
    while True:
        print("\n***** MENU CLIENTE *****")
        print("1. Ver saldo")
        print("2. Ver sessões")
        print("3. Comprar ingressos")
        print("4. Adicionar saldo")
        print("5. Deslogar e retornar ao menu anterior")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            ver_saldo(cliente)

        elif opcao == "2":
            ver_sessoes(sessoes)

        elif opcao == "3":
            sessao_selecionada = selecionar_sessao(sessoes)
            comprar_ingressos(sessao_selecionada, cliente)

        elif opcao == "4":
            adicionar_saldo(cliente)

        elif opcao == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Deslogando")
            break

        else:
            print("Opção inválida.")


while True:
    print("\n***** CINEMA *****")
    print("1. Login")
    print("2. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome_cliente = input("Digite o nome do cliente: ")
        cliente_encontrado = False

        for cliente in clientes:
            if cliente.nome == nome_cliente:
                menu_cliente(cliente)
                cliente_encontrado = True

        if not cliente_encontrado:
            print("Cliente não encontrado.")

    elif opcao == "2":
        print("Obrigado por utilizar nosso sistema de venda de ingressos. Volte sempre!")
        os.system('cls' if os.name == 'nt' else 'clear')
        break

    else:
        print("Opção inválida.")
