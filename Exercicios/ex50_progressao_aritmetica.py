'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
 No final, mostre os 10 primeiros termos dessa progressão.'''

first_term = int(input('Escreva o primeiro termo da sua PA: '))
progressionRatio = int(input('Digite o tamanho do intervalo da PA: '))
totalElements = int(input('Digite o total de elementos da sua PA: '))
last_term = first_term + (totalElements-1)*progressionRatio

# for i in range (first_term,totalElements):
#     print(f'{first_term + i * progressionRatio} ',end='')

# Outra forma
for i in range (first_term,last_term + 1,progressionRatio):
    print(f'{i}', end =' - ')

print('Fim')