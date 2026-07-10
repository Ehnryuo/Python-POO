from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    """Cria uma estrutura onde é possível calcular salários de funcionarios diferentes - horista ou mensalista"""
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0



    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self):
        base = self.salario / Funcionario.sal_min

        mensagem = f'O salário de [blue]{self.nome}[/]({self.__class__.__name__}) é de [green on yellow]R${self.salario:.2f}[/] e corresponde a {base:.1f} salários mínimos'
        painel = Panel(mensagem, title='Análise de Salário', width=50)
        print(painel)



class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, horas_trabalhadas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas
        self.sal_bruto = self.valor_hora * self.horas_trabalhadas

    def calc_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)



class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto = Funcionario.sal_min):
        super().__init__(nome)

        self.sal_bruto = sal_bruto

    def calc_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
