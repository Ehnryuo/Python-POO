from rich import print
from rich.traceback import install
install()

class Livro():
    """Uma classe onde é possível avançar e voltar as páginas de um livro"""
    def __init__(self, titulo, pagina_atual, qtd_pagina):
        self.pagina_atual = pagina_atual
        self.qtd_pagina = qtd_pagina
        self.titulo = titulo

    def avancar_pagina(self, n = 1):
        if self.pagina_atual + n > self.qtd_pagina:
            self.pagina_atual = self.qtd_pagina
            return print(f'O livro tem apenas [red]{self.qtd_pagina} páginas[/], você chegou ao final do livro: {self.titulo}')
        else:
            self.pagina_atual += n
            return print(f'Você avançou {n} páginas e agora está na página {self.pagina_atual}')


    def voltar_pagina(self, n = 1):
        if self.pagina_atual - n <= 0:
            self.pagina_atual = 1
            return print(f'Você voltou para o início do livro! {self.titulo}')
        else:
            self.pagina_atual -= n
            return print(f'Você voltou para a página {self.pagina_atual} do livro de {self.titulo}')

leitor1 = Livro(titulo= "[purple]:white_medium_star:  Soul Eater!!", pagina_atual=1, qtd_pagina=20)
leitor1.avancar_pagina(19)
leitor1.voltar_pagina(9)