from rich import inspect

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) #Este comando faz com que a classe mãe seja chamada
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} fez a matrícula!')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'Aula do Professor: {self.nome}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_pontos(self):
        print(f'A funcionária {self.nome} acabou de bater ponto.')

a1 = Aluno('josé', '25', 'Ti', '902b')
#inspect(a1)
p1 = Professor('Renato', '42', 'Matemática', 'Mestrado')
p1.dar_aula()
inspect(p1, methods=True)
