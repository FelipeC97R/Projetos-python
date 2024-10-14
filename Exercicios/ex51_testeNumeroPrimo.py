'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

UserNumber = int(input('Digite um número inteiro: '))
countFactors = 0

print('Numeros disiveis:')
for i in range (2,UserNumber):
    if UserNumber % i == 0:
        print(f'\033[34m',end='')
        countFactors += 1
    else:
        print(f'\033[32m',end='')
    print(f'{i}',end=' ')

print(f'\033[m\nEle possui {countFactors} números divisiveis')
if countFactors == 0 :
    print(f'{UserNumber} é um número primo')
else: 
    print(f'{UserNumber} não é um número primo.')