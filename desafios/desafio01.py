class Funcionario():

    """Esta classe cadastra um funcionário, mantendo registrado seu nome, cargo e setor"""

    def __init__(self, cargo = 'vazio', nome = 'vazio', setor = 'vazio'):
        self.cargo = cargo
        self.nome = nome
        self.setor = setor

    #Quando der o print no objeto, a frase abaixo será exibida
    def __str__(self):
        return f'Meu nome é {self.nome}, sou do setor {self.setor} e meu cargo é {self.cargo}'

fun1 = Funcionario(cargo = 'assistente admnistrativo financeiro', nome = 'Lucas', setor = 'financeiro')
print(fun1)