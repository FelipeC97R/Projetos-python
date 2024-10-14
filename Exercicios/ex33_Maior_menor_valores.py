'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = int(input('Escreva o primeiro número: '))
n2 = int(input('Escreva o segundo número: '))
n3 = int(input('Escreva o terceiro número: '))

menor = n1
maior = n1 
if n3 <= n1 and n3 <= n2:
    menor = n3

if n2 >= n1:
    maior = n2
if n2 <= n1 and n2 <= n3:
    menor = n2 
if n3 >=n1:
    maior = n3

print(f'O menor é {menor} e o maior é {maior}')