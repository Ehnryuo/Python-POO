from ex010 import *
from rich import inspect
av1 = Avaliacao('Pedro', 'Matemática')
av1.set_nota(821)
print(f'{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}')
inspect(av1, private=True)