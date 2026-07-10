# declaração de classe
class Gafanhoto(): # método construtor
    """
    Esta classe cria um "gafanhoto", que é uma pessoa que tem nome e idade
    """
    def __init__(self, nome = 'vazio', idade = 0): #obs: caso coloque algo para "passar" nos parâmetros, se torna algo opicional e não obrigatório ex: n = '', i = 0
        self.nome = nome
        self.idade = idade

    # métodos da classe
    def aniversario(self):
        self.idade += 1

    def __str__(self): #Dunder Method
        return f'Seu nome é {self.nome} e sua idade é {self.idade}'

    def __getstate__(self):
        return f'Nome: {self.nome}; idade: {self.idade}'


# declaração de objetos

pessoa1 = Gafanhoto(nome='Lucas', idade=20)

pessoa1.aniversario()
print(pessoa1)

pessoa2 = Gafanhoto()
print(pessoa2)

print(pessoa1.__doc__) #Dunder Attribute

print(pessoa1.__dict__) #Attribute - deixa no formato de dicionário

print(pessoa1.__getstate__()) #Method

print(pessoa1.__class__)
