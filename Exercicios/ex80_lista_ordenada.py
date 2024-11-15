'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

numerosInteiro = []

for num in range(0,5):
    numerosInteiro.append(int(input('Digite um número: ')))

print(len(numerosInteiro))


# Bubble Sort
for i in range(len(numerosInteiro)-1):
    for j in range(len(numerosInteiro)-1,i+1,-1):
        if numerosInteiro[j] < numerosInteiro[j-1]:
            aux = numerosInteiro[j]
            numerosInteiro[j] = numerosInteiro [j-1]
            numerosInteiro[j-1] = aux


print(numerosInteiro)