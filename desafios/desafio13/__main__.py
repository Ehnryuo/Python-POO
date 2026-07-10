from termostato import *
from rich import inspect


def main():


    termostato = Termostato()

    inspect(termostato, private=True)

    print(termostato.ftemperatura)

    termostato.aumentar()
    print(termostato.ftemperatura)

    termostato.diminuir()
    print(termostato.ftemperatura)

    termostato.temperatura = 29.5
    print(termostato.ftemperatura)

if __name__ == '__main__':
    main()