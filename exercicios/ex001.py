#escopo / classe / modelo
class Gafanhoto():
    def __init__(self):
        self.nome = ''
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        print(f'Seu nome é {self.nome} e sua idade é {self.idade}')

#objetos e atributos

pessoa1 = Gafanhoto()

pessoa1.nome = 'Lucas'
pessoa1.idade = 20
pessoa1.aniversario()
pessoa1.mensagem()