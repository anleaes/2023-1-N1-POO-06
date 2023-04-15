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