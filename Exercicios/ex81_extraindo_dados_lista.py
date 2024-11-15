'''Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

numbersInteger = []
print(len(numbersInteger))
while True:
    numbersInteger.append(int(input('Digite um número inteiro: '))) 
    
    addMoreNumbers = input('Gostaria de adicionar mais um número? [s/n]: ').lower().strip()
    if addMoreNumbers == 'n':
        break

print(f'Total de números digitados: {len(numbersInteger)}')
numbersInteger.sort()
print(f'Lista em ordem: {numbersInteger}')

if 5 not in numbersInteger:
    print('Não há número 5 na lista')
else:
    print(f'Total de números 5 na lista: {numbersInteger.count(5)}')