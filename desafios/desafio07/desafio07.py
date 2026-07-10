from rich import print
from rich.traceback import install
from rich.panel import Panel

install()

class Televisao():
    """Uma classe que representa uma televisão, ela começa desligada e quando ligada,
        terá opções para mudar de canal e ajustar o volume dela"""
    def __init__(self, comandos):
        self.comandos = comandos
        self.tv = False
        self.canais = [1,2,3,4,5]
        self.canal_atual = 1
        self.volume = 2

    def mostrar_painel(self):
        canais_str = ""

        for i in self.canais:

            if i == self.canal_atual:
                canais_str += f"[black on yellow] {i} [/] "
            else:
                canais_str += str(i) + " "

        barra_volume = "[cyan]"

        for i in range(self.volume):
            barra_volume += "█"

        barra_volume += "[/cyan][grey35]" #Isso diz ao Rich: pare de pintar de azul e comece a pintar de cinza

        for i in range(5 - self.volume):
            barra_volume += "█"

        barra_volume += "[/grey35]"

        texto = f"CANAL  = {canais_str}\nVOLUME = {barra_volume}"

        print(Panel(texto, title="[ TV ]", expand=False))

    def Controle(self):
        print(Panel("[red]A televisão está desligada!", title="Tv", expand=False))

        while not self.tv:

            ligar = input("Digite @ para ligar a TV: ")

            if ligar == '@':
                self.tv = True

        print('\n' * 3)
        self.mostrar_painel()

        while True:
            a = input("< CH1 >   - VOL2 + : ")

            if a == '<':
                if self.canal_atual == 1:
                    print("Você já está no canal 1!")
                else:
                    self.canal_atual -= 1

            elif a == '>':
                if self.canal_atual == self.canais[-1]:
                    print("Você já está no último canal!")
                else:
                    self.canal_atual += 1

            elif a == '+':
                if self.volume < 5:
                    self.volume += 1
                else:
                    print("Volume máximo!")

            elif a == '-':
                if self.volume > 0:
                    self.volume -= 1
                else:
                    print("Volume mínimo!")

            self.mostrar_painel()

controle1 = Televisao('')
controle1.Controle()