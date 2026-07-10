class Diario:
    """Uma classe que simula o funcionamento de um diário, sendo possível ler apenas com a senha."""
    def __init__(self, senha):
        self.__segredos = []
        self.__senha = senha

    def escrever(self, msg):
        self.__segredos.append(msg)
        pass

    def ler(self, senha):
        if senha == self.__senha:
            for i in self.__segredos:
                print(f'{i}')
        else:
            raise ValueError('Senha incorreta!')