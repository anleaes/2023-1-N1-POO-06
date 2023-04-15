from cliente import Cliente
from filme import Filme
from sessao import Sessao

# Criando os objetos Filme
filme1 = Filme("O Poderoso Chefão", "2h 58min", "Drama", "16 anos")
filme2 = Filme("Toy Story", "1h 21min", "Animação", "Livre")
filme3 = Filme("Os Vingadores", "2h 23min", "Ação", "12 anos")
filme4 = Filme("A Lista de Schindler", "3h 15min", "Drama", "14 anos")
filme5 = Filme("Harry Potter e a Pedra Filosofal", "2h 32min", "Fantasia", "10 anos")

# Criando as sessões referenciando os objetos Filme criados anteriormente
sessao1 = Sessao(filme1, "18h", 20.0, 100, 0, [])
sessao2 = Sessao(filme1, "21h", 25.0, 50, 0, [])
sessao3 = Sessao(filme2, "14h", 15.0, 80, 0, [])
sessao4 = Sessao(filme2, "17h", 18.0, 60, 0, [])
sessao5 = Sessao(filme3, "19h", 22.0, 120, 0, [])
sessao6 = Sessao(filme3, "22h", 28.0, 70, 0, [])
sessao7 = Sessao(filme4, "15h", 17.0, 90, 0, [])
sessao8 = Sessao(filme4, "18h", 20.0, 70, 0, [])
sessao9 = Sessao(filme5, "16h", 18.0, 100, 0, [])
sessao10 = Sessao(filme5, "20h", 25.0, 60, 0, [])


cliente1 = Cliente("João", "123.456.789-00", "(11) 99999-9999", 50.0, "1111 2222 3333 4444", 25)
cliente2 = Cliente("Maria", "987.654.321-00", "(11) 88888-8888", 100.0, "5555 6666 7777 8888", 30)
cliente3 = Cliente("Roberta", "432.632.734-42", "(51) 98644-5732", 60.00, "7384 6127 8743 6532", 23)
cliente4 = Cliente("Rodrigo", "532.627.236-43", "(51) 98563-2714", 120.00, "2421 5326 2634 6324", 19)
cliente5 = Cliente("Pedro", "754.845.326-24", "(51) 98889-4256", 300.00, "6327 5365 3267 3626", 42)
cliente6 = Cliente("Lucas", "443.255.743-87", "(57) 98632-4323", 520.00, "7345 8669 5889 5696", 33)
cliente7 = Cliente("Yasmin", "842.745.784-24", "(51) 99632-6356", 230.00, "3652 3267 8659 6055", 22)
cliente8 = Cliente("Laís", "632.743.976-39", "(51) 99652-7374", 90.00, "8754 3845 5963 5944", 29)
cliente9 = Cliente("Roger", "637.845.842-12", "(51) 98094-0924", 300.00, "3458 8735 3786 8459", 30)
cliente10 = Cliente("Julia", "326.237.743-23", "(51) 99375-0093", 430.50, "3547 3485 9659 6574", 31)

cliente1.comprar_ingresso(sessao1, 2)
cliente2.comprar_ingresso(sessao1, 3)

# Assuming you have a Filme object called 'filme1'
print("Título: ", filme1.nome)
print("Duração: ", filme1.duracao)
print("Gênero: ", filme1.genero)
print("Classificação indicativa: ", filme1.classificacao)
