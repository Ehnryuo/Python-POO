from rich import print
from rich.traceback import install
from rich.panel import Panel

install()

# Considerar 400g por pessoa e Preço: R$82,40 kg
class Churrasco:
    def __init__(self, quantidade):
        self.quantidade = quantidade
        self.recomendado = 400 * quantidade / 1000  # em Kg
        self.total = 82.40 * self.recomendado
        self.totalpessoa = self.total / self.quantidade

    def analise(self):
        texto = (
            f"[purple]Com {self.quantidade} convidados: [/]\n"
            f"[blue]- Cada participante comerá 0.4Kg\n"
            f"- Recomendo comprar {self.recomendado:.2f} Kg de carne\n"
            f"- O custo total será R$ {self.total:.2f}\n"
            f"- Cada pessoa pagará R$ {self.totalpessoa:.2f}"
        )
        print(Panel(texto, title="Custo do Churrasco", expand=False))

        # faz com que o painel se ajuste ao tamanho do texto, em vez de ocupar toda a largura do terminal

churrasco1 = Churrasco(quantidade=15)
churrasco1.analise()