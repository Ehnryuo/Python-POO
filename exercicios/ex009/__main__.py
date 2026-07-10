from ex009 import ContaBancaria
pessoa1 = ContaBancaria(id = 93, nome= 'Lucas', saldo=3000)
pessoa1.deposito(200)


pessoa1.titular = 'pedro' #Ao colocar um _ antes do "titular", é possível alterar o atributo protegido, mas não mexa..
pessoa1._ContaBancaria__saldo = 0 #Ao chamar o _"nome da classe"__"atributo" é possível alterar mesmo ela sendo PRIVADA
#Podemos acompanhar a mudança sendo feita pelo comando que fizemos no ex009 return f'Estado atual da conta: {self.__dict__}' que nos retorna um dicionário com as informações contidas nele

#Adultos não fazem tais alterações, isso é o que foi acordado.
print(pessoa1)