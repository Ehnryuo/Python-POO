from rich import inspect
from classes import Aluno, Professor, Funcionario

a1 = Aluno('josé', '25', 'Ti', '902b')
#inspect(a1)
p1 = Professor('Renato', '42', 'Matemática', 'Mestrado')
p1.dar_aula()
inspect(p1, methods=True)
f1 = Funcionario('Cláudia', '27', 'Secretária', 'Administrativo')
f1.bater_pontos()

a1.estudar()
p1.estudar()
f1.estudar()