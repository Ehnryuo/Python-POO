from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, tamanho_lado):
        super().__init__(4)  # chama o construtor da classe base
        self.tamanho_lado = tamanho_lado

    def perimetro(self):
        return 4 * self.tamanho_lado

    def area(self):
        return self.tamanho_lado ** 2

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)  # círculo não tem lados
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2
