'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira'''
import math
num = float(input('Digite um número : '))
print(f'O valor inteiro é {math.trunc(num)}')