class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str, saldo: float, cartao_credito: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.saldo = saldo
        self.cartao_credito = cartao_credito
        self.idade = idade

    def adicionar_saldo(self, valor: float):
        self.saldo += valor

    def comprar_ingresso(self, sessao, qtd_ingressos):
        valor_total = sessao.preco * qtd_ingressos
        if valor_total > self.saldo:
            print("Saldo insuficiente para realizar a compra")
        elif qtd_ingressos > sessao.ingressos_disponiveis:
            print("Não há ingressos disponíveis suficientes para realizar a compra")
        else:
            print(f'{qtd_ingressos:.0f} ingressos adquiridos com sucesso')
            sessao.vender_ingressos(qtd_ingressos)
            self.saldo -= valor_total
            sessao.adicionar_cliente(self)
