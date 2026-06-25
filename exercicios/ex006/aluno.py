from pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) #Este comando faz com que a classe mãe seja chamada
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} fez a matrícula!')