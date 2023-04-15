from cliente import Cliente
from filme import Filme
from sessao import Sessao

filme = Filme("O Poderoso Chefão", "2h 58min", "Drama", "16 anos")

sessao1 = Sessao(filme, "18h", 20.0, 100, 0, [])
sessao2 = Sessao(filme, "21h", 25.0, 50, 0, [])

cliente1 = Cliente("João", "123.456.789-00", "(11) 99999-9999", 50.0, "1111 2222 3333 4444", 25)
cliente2 = Cliente("Maria", "987.654.321-00", "(11) 88888-8888", 100.0, "5555 6666 7777 8888", 30)

cliente1.comprar_ingresso(sessao1, 2)
cliente2.comprar_ingresso(sessao1, 3)
cliente2.comprar_ingress