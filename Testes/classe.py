class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str, saldo: float, cartao_credito: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.saldo = saldo
        self.cartao_credito = cartao_credito
        self.idade = idade
        
    def depositar_saldo(self, valor: float) -> None:
        self.saldo += valor
        
    def comprar_ingresso(self, sessao: Sessao, qtd_ingressos: int) -> None:
        if sessao.ingressos_disponiveis >= qtd_ingressos and self.saldo >= sessao.preco * qtd_ingressos:
            sessao.vender_ingressos(qtd_ingressos)
            self.saldo -= sessao.preco * qtd_ingressos
            sessao.adicionar_cliente(self)
            print(f"Ingresso(s) comprado(s) com sucesso para a sessão do filme {sessao.filme.nome}.")
        else:
            print("Não foi possível comprar o(s) ingresso(s). Saldo insuficiente ou ingressos esgotados.")
            

class Filme:
    def __init__(self, nome: str, duracao: str, genero: str, classificacao: str):
        self.nome = nome
        self.duracao = duracao
        self.genero = genero
        self.classificacao = classificacao
        

class Sessao:
    def __init__(self, filme: Filme, horario: str, preco: float, ingressos_disponiveis: int, ingressos_vendidos: int, clientes: list[Cliente]):
        self.filme = filme
        self.horario = horario
        self.preco = preco
        self.ingressos_disponiveis = ingressos_disponiveis
        self.ingressos_vendidos = ingressos_vendidos
        self.clientes = clientes
        
    def vender_ingressos(self, qtd: int) -> None:
        self.ingressos_disponiveis -= qtd
        self.ingressos_vendidos += qtd
        
    def adicionar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)
