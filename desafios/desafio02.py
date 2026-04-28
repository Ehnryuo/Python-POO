from rich import print
from rich.table import Table
from rich.traceback import install
install()

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def produto(self):
        #Adiciona o título da tabela..
        self.tabela = Table(title=f'Produto')

        #Adiciona uma coluna na tabela
        self.tabela.add_column(self.nome, justify='center')

        #Adiciona uma linha/fileira na tabela
        self.tabela.add_row(self.preco)
        return print(self.tabela)
p1 = Produto('Iphone 17', '5000')
p1.produto()
p2 = Produto('Applewatch', '250')
p2.produto()