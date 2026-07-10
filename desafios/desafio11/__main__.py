from funcionario import *
from rich import inspect


def main():
    f1 = Horista('Pedro', 12, 190)
    f1.calc_salario()
    f1.analisar_salario()

if __name__ == '__main__':
    main()