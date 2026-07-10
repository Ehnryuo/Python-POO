from diario import *
from rich import inspect

pessoa1 = Diario('Samurai')
pessoa1.escrever('Hoje eu estudei muito, de tarde eu aproveitei para jogar um Cyberpunk 2077')
pessoa1.escrever('Também fiz uma caminhada a noite')

pessoa1.ler('Samurai')

inspect(pessoa1, private=True, methods=True)