from abc import ABC, abstractmethod
class BebidaQuente(ABC):
    """Uma classe que simula uma cafeteira, podendo servir café, chá ou leite"""
    @abstractmethod
    def __init__(self):
        pass

    def preparar(self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('--- Bebida Pronta ---')

    def ferver_agua(self):
        print(f'Fervendo água a 100 graus Celcius')

    @abstractmethod
    def misturar(self):     #Cada bebida, a mistura é feita de forma diferente
        pass

    @abstractmethod
    def servir(self):       #Cada bebida, é servida de forma diferente
        pass


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()
    def misturar(self):
        print(f'Passando água pressurizada pelo pó de café moído.')

    def servir(self):
        print(f'Servindo em xícara pequena.')


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print(f'Mergulhando o sachê de ervas na água.')

    def servir(self):
        print(f'Servindo na caneca de porcelana com limão.')


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print(f'Passando vapor pressurizado pelo bico de leite.')

    def servir(self):
        print(f'Servindo na caneca grande, já com café.')