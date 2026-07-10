from ex011 import *
from rich import inspect
av1 = Avaliacao('Pedro', 'Matemática')
av1.nota = 3.5
print(f'{av1.nome} tirou {av1.nota} em {av1.disciplina}')
inspect(av1, private=True) #Podemos observar que ao rodar o código, o "nota" tá dando acesso ao "_nota" (atributo protegido)