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