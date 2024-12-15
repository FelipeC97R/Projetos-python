'''4- Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''


# num_1 = int(input('numero 1: '))
# num_2 = int(input('numero 2: '))
# num_3 = int(input('numero 3: '))

num_1 = 2
num_2 = 6
num_3 = 4

maior = num_1
menor = num_2

if num_1 < num_2:
    maior = num_2
    menor = num_1
    if num_3 > num_2:
        maior = num_3
    if num_3 < num_1:
        menor = num_3

print (maior)