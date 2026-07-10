# Declaração de Classe
class ContaBancaria:
    """
    Cria uma classe onde permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso, seu saldo atual é de R${self.saldo}')

    def __str__(self):
        return f'A conta com id {self.id} de {self.titular}, tem R${self.saldo:,.2f} de saldo'


    def saque(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            return self.saldo
        else:
            return f'Você não tem essa quantia para sacar...'


    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado')



# Declaração de objetos
pessoa1 = ContaBancaria(id = 93, nome= 'Lucas', saldo=3000)
print(pessoa1.saque(3500))
pessoa1.deposito(200)
print(pessoa1)