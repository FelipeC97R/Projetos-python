'''Faça um programa que receba um número e mostre a sua tabuada até 10'''
from time import sleep

print('*'*5,'Gerador de Tabuadas','*'*5)

UserChoosedNumber = int(input('Digite um número da sua tabuada: '))
tableRange = int (input('Valor máximo da sua tabuada: '))
print('Gerando tabuada ...')
sleep(2)
print('-='*10,f'TABUADA do {UserChoosedNumber}','-='*10,'\n')
sleep(1)
for i in range(1,tableRange + 1):
    print(' '*20,f'{UserChoosedNumber} X {i:2}   = {i*UserChoosedNumber}')
    sleep(1)

print('\n*FIM*\n')
input('Pressione qualquer tecla para finalizar ...')