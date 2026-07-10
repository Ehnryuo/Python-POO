from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        fator = float
        pass

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)
        print(self.calc_frete())

    def calc_frete(self):
        valor = self.fator * self.distancia
        return f'Frete de {Moto.__name__} em {self.distancia}km = {valor:.2f}R$'


class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)
        if distancia < 50:
            print(f'Frete do Caminhão em {distancia}, o minímo é de 50km')
        else:
            print(f'Frete de {Caminhao.__name__} em {distancia}km = {valor:.2f}R$')

    def calc_frete(self):
        valor = distancia * fator
        return valor


class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia):
        super().__init__(distancia)
        if distancia > 10:
            print('A bateria do drone não suporta a distância informada')
        else:
            print(f'Frete de {Drone.__name__} em {distancia}km = {valor:.2f}R$')

    def calc_frete(self):
        valor = distancia * fator
        return valor
