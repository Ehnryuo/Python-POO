from rich import print
from rich.traceback import install
install()

#a importação acima faz com que a visualização de erro, seja mais clara

def divisao(n1, n2):
    return n1 / n2

print(divisao(50, 0))