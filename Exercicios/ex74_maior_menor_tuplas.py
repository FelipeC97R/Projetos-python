''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
 Depois disso, mostre a listagem de números gerados 
 e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

randomNumbers = tuple(randint(0,100)for _ in range(5))
print('Números da tupla: ',end='')
for num in randomNumbers:
    print(f"{num} ",end='')
print(f'\nmenor valor : {min(randomNumbers)}')
print(f'Maior valor : {max(randomNumbers)}')