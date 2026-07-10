from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Gamer():
    """
    Uma função que cadastra o nome e nickname de um player e mostra sua ficha com
    seus jogos favoritos em um painel.
    """
    def __init__(self, nome, nickname):
        #foi inserido uma lista para que o método da classe não guardasse apenas o último jogo cadastrado
        self.nome = nome
        self.nickname = nickname
        self.favoritoslist = []

    def favoritos(self, jogos):
        #Adicionando itens a lista....
        self.favoritoslist.append(jogos)

    def ficha(self):
        #O .join() é um método de string que serve para concatenar os elementos
        # de uma lista em uma única string, colocando entre cada elemento o separador que
        # você escolher (no caso \n para quebrar as linhas.

        jogos = "\n".join(self.favoritoslist)
        texto = (
            f'Nome real: {self.nome} \n'
            f'Jogos favoritos: [red]\n{jogos}'
        )
        print(Panel(texto, title=f'[purple]Jogador: {self.nickname}', expand=False))

player1 = Gamer('Lucas ', 'Seu amor')
player1.favoritos('Red Dead Redemption 2')
player1.favoritos('Forza Horizon 6')
player1.favoritos('Persona 5 Royal')
player1.ficha()