class ContaBancaria:
    """
    Cria uma classe onde permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id # público (+)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        print(f'Conta {self.id} criada com sucesso, seu __saldo atual é de R${self.__saldo}')

    def __str__(self):
        #return f'A conta com id {self.id} de {self._titular}, tem R${self.__saldo:,.2f} de __saldo'
        return f'Estado atual da conta: {self.__dict__}'

    def saque(self, valor):
        valor = abs(valor)
        if self.__saldo > valor:
            self.__saldo -= valor
            return self.__saldo
        else:
            return f'Você não tem essa quantia para sacar...'


    def deposito(self, valor):
        valor = abs(valor) #vai considerar só os valores positivos (não será possível depositar - R$500,00 exemplo.
        self.__saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado')



