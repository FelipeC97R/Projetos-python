'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
 em uma lista única que mantenha separados os valores pares e ímpares.
   No final, mostre os valores pares e ímpares em ordem crescente.'''

lista_numeros = [[],[]]
for i in range (7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        lista_numeros[1].append(numero)
    else:
        lista_numeros[0].append(numero)


lista_numeros[1].sort()
lista_numeros[0].sort()

print(lista_numeros)