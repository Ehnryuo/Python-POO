from rich import print
from rich.traceback import install
install()

class Caneta():
    """Uma classe que vai simular o funcionamento de uma caneta colorida,
    você vai poder destampar, trocar as cores e escrever frases em sua devida cor """
    def __init__(self, frase):
        self.frase = frase
        self.tampada = True
        self.newcolor = 'white'

    def Cor(self, newcolor):
        self.newcolor = newcolor

    def TamparCaneta(self):
        self.tampada = True
        print('A caneta foi tampada com sucesso!')

    def DestamparCaneta(self):
        self.tampada = False
        print('A caneta foi destapada com sucesso!')

    def Escrever(self):
        if self.tampada == True:
            return f'A caneta está tampada e não é possivel escrever'
        else:
             print(f'[{self.newcolor}]{self.frase}[/{self.newcolor}]')

    def QuebrarLinha(self, numero):
        print('\n' * numero, end='')

c1 = Caneta('Eu amo jogar!')
c1.Cor('purple')
c1.DestamparCaneta()
c1.Escrever()
c1.QuebrarLinha(1)
c2 = Caneta('Eu amo comer nos finais de semana.')
c2.Cor('blue')
c2.DestamparCaneta()
c2.Escrever()