from rich import print
from rich.panel import Panel

#para fazer uso do emoji é necessário o uso dos ::
#python -m rich.emoji o comando para ser utilizado no terminal e ter conhecimento dos emojis habilitados
caixa = Panel('[blue]Este é um painel de exemplo :+1:', title='Exemplo', style='purple')
print(caixa)