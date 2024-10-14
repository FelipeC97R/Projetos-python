'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

import os
sexUser = ' '
while sexUser not in 'FM':
    sexUser = str(input('Digite o seu sexo: ')).upper().strip()[0]
    os.system ('cls')
    if sexUser not in 'FM':
        print('Valor inválido! digite novamente.')
print(f'Sexo: {sexUser}')