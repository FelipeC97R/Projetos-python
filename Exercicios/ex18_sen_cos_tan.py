'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e 
tangente desse ângulo.'''
from math import sin,cos,tan,radians
ang = radians(float(input('Digite o valor de um angulo em graus: ')))
print(f'Seno: {sin(ang):.2f}\n'
      f'Cosseno: {cos(ang):.2f}\n'
      f'Tangente: {tan(ang):.2f}')


