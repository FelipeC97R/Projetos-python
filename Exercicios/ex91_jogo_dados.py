'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
 sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

todos_jogadores = {'Pedro':randint(1,6),
                   'Ana':randint(1,6),
                   'João':randint(1,6),
                   'Pamela':randint(1,6)}

print(todos_jogadores.items())

for nome, resultado in todos_jogadores.items():
    print(f'{nome} tirou {resultado}')
    sleep(0.5)

print('-'*40)
ranking = {}
ranking = sorted(todos_jogadores.items(), key=itemgetter(1), reverse=True)

print(ranking)
for posicao, (nome, resultado) in enumerate(ranking, 1):
    print(f'{posicao}ºlugar: {nome} com {resultado}')
    sleep(0.5)
