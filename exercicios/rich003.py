from rich import print
from rich.table import Table

#adiciona o título da tabela
tabela = Table(title='Tabela de Preços')

#Adiciona uma coluna

tabela.add_column('Nome', justify='right')
tabela.add_column('Preço', justify='center')

#Adiciona um produto

tabela.add_row('Ssd', '250')
tabela.add_row('Mouse', '[red]300')

print(tabela)