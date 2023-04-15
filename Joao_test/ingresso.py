class Ingresso:
    def __init__(self, id, horario, filme, sala, lugar, pessoa):
        self.id = id
        self.horario = horario
        self.filme = filme
        self.sala = sala
        self.lugar = lugar
        self.pessoa = pessoa
        self.filme_obj = Filme(filme_id, filme_nome, filme_genero, filme_duracao, filme_idade, sala_obj)

    def comprar(self):
        self.pessoa.comprar(self)
