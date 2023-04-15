from cliente import Cliente
from filme import Filme
from sessao import Sessao

def listar_sessoes(sessoes):
    print("Sessões disponíveis:")
    for i, sessao in enumerate(sessoes):
        print(f"{i+1}. {sessao.filme.nome} - Horário: {sessao.horario} - Preço: R${sessao.preco} - Ingressos disponíveis: {sessao.ingressos_disponiveis}")

def comprar_ingressos(sessao, cliente):
    qtd_ingressos = int(input("Quantos ingressos deseja comprar? "))
    cliente.comprar_ingresso(sessao, qtd_ingressos)


# Criação de objetos Filme, Sessao e Cliente
filme1 = Filme("O Poderoso Chefão", "2h 58min", "Drama", "16 anos")
filme2 = Filme("Toy Story", "1h 21min", "Animação", "Livre")
filme3 = Filme("Os Vingadores", "2h 23min", "Ação", "12 anos")

sessao1 = Sessao(filme1, "18h", 20.0, 100, 0, [])
sessao2 = Sessao(filme1, "21h", 25.0, 50, 0, [])
sessao3 = Sessao(filme2, "14h", 15.0, 80, 0, [])

cliente1 = Cliente("João", "123.456.789-00", "(11) 99999-9999", 50.0, "1111 2222 3333 4444", 25)
cliente2 = Cliente("Maria", "987.654.321-00", "(11) 88888-8888", 100.0, "5555 6666 7777 8888", 30)
cliente3 = Cliente("Roberta", "432.632.734-42", "(51) 98644-5732", 60.00, "7384 6127 8743 6532", 23)

# Lista de sessões disponíveis
sessoes_disponiveis = [sessao1, sessao2, sessao3]

# Lista de clientes cadastrados
clientes_cadastrados = [cliente1, cliente2, cliente3]

    # Loop do menu
while True:
    print("\n***** CINEMA *****")
    print("1. Ver sessões disponíveis")
    print("2. Comprar ingressos")
    print("3. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        listar_sessoes(sessoes_disponiveis)
        
    if opcao == "2":
        # Seleciona a sessão desejada pelo usuário
        listar_sessoes(sessoes_disponiveis)
        sessao_opcao = int(input("Selecione a sessão desejada: ")) - 1
        sessao_selecionada = sessoes_disponiveis[sessao_opcao]
            # Verifica se a sessão tem ingressos disponíveis
        if sessao_selecionada.ingressos_disponiveis == 0:
            print("Não há ingressos disponíveis para esta sessão.")
        else:
            # Seleciona o cliente que irá comprar os ingressos
            for i, cliente in enumerate(clientes_cadastrados):
                print(f"{i+1}. {cliente.nome} - Saldo: R${cliente.saldo}")
            cliente_opcao = int(input("Selecione o cliente desejado: ")) - 1
            cliente_selecionado = clientes_cadastrados[cliente_opcao]

            # Realiza a compra de ingressos pelo cliente selecionado
            comprar_ingressos(sessao_selecionada, cliente_selecionado)
        
    if opcao == "3":
        print("Obrigado por utilizar nosso sistema de venda de ingressos. Volte sempre!")
        break
    
    
