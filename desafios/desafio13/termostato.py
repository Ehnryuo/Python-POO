class Termostato:
    def __init__(self, temperatura=24):
        self.__temperatura = 24      # valor inicial
        self.temperatura = temperatura   # passa pelo setter

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError("A temperatura deve variar de 0.5 em 0.5.")

        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"

    def aumentar(self):
        self.temperatura += 0.5

    def diminuir(self):
        self.temperatura -= 0.5
