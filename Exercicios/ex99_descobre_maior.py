'''Faça um programa que tenha uma função chamada maior(),
 que receba vários parâmetros com valores inteiros. 
 Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from random import randint

def maior(numeros):
    print(max(numeros))

valores = []
for i in range (randint(2,10)):
    valores.append(randint(1,100)) 

print(valores)
print(maior(valores))