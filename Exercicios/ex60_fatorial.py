'''Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''

from math import factorial
from time import sleep
print('='*30,f'\n{'GERADOR DE FATORIAL':^30}\n','='*30)
sleep(1)
while True:
    number = int(input('\nDigite um número para descobrir o seu fatorial: '))

    print('\nGerando fatorial...')
    sleep(2)
    print(f'\n{number} ! = {number} ', end = '')
    counter = number -1
    while counter != 0 :
        print(f'X {counter}  ', end = '',flush = True)
        counter -= 1
        sleep(0.1)
    print(f'= {factorial(number):,}'.replace(',','.'))
    sleep(1)
    while True:
        tryOtherNumber = input('\nGostaria de ver outro número [s/n]:').lower()
        if tryOtherNumber in ('s','n'):
            break
        print('Valor inválido, tente novamente')
    if tryOtherNumber == 'n':
        break