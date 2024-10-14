'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.'''

import math 
triangleOppositeSide = int(input('Quanto mede o cateto oposto: '))
triangleAdjacentSide = int(input('Quanto mede o cateto oposto: '))
triangle_hypotenuse = math.hypot(triangleOppositeSide,triangleAdjacentSide)
print (f' A hipotenusa vale: {triangle_hypotenuse}')