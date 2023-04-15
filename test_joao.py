class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str, saldo: float, cartao_credito: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.saldo = saldo
        self.cartao_credito = cartao_credito
        self.idade = idade

    def depositar_saldo(self, valor: float):
        self.saldo += valor

    def comprar_ingresso(self, sessao, qtd_ingressos):
        valor_total = sessao.preco * qtd_ingressos
        if valor_total > self.saldo:
            print("Saldo insuficiente para realizar a compra")
        elif qtd_ingressos > sessao.ingressos_disponiveis:
            print("Não há ingressos disponíveis suficientes para realizar a compra")
        else:
            sessao.vender_ingressos(qtd_ingressos)
            self.saldo -= valor_total
            sessao.adicionar_cliente(self)

class Filme:
    def __init__(self, nome: str, duracao: str, genero: str, classificacao: str):
        self.nome = nome
        self.duracao = duracao
        self.genero = genero
        self.classificacao = classificacao

from cliente import Cliente
from filme import Filme

class Sessao:
    def __init__(self, filme: Filme, horario: str, preco: float, ingressos_disponiveis: int, ingressos_vendidos: int, clientes: list[Cliente]):
        self.filme = filme
        self.horario = horario
        self.preco = preco
        self.ingressos_disponiveis = ingressos_disponiveis
        self.ingressos_vendidos = ingressos_vendidos
        self.clientes = clientes

    def vender_ingressos(self, qtd: int):
        self.ingressos_disponiveis -= qtd
        self.ingressos_vendidos += qtd

    def adicionar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
