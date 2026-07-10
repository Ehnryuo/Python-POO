class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota #Atributo protegido

        #Criando atributo validável.

        @property # De baixo do property, colocar um método com o mesmo nome do atributo que vc deseja e o código do getter
        def nota(self): #Getter
            return self._nota #código do getter
        @nota.setter
        def nota(self, valor): #setter
            if 0 <= valor <= 10:
                self._nota = valor
            else:
                print('Nota inválida!')

        @nota.deleter   #Se eu tentar apagar apagar o atributo, ele pode executar o método abaixo, exemplo: você só pode excluir esse atributo se passar por algum tipo de validação
        def nota(self):
            pass