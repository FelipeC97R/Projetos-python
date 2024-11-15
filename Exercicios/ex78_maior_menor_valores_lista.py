'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
 mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

numeros = [1,1,6,8,2,8]
# numeros = []
# for num in range(0,5):
#     numeros.append(int(input('Digite um número:')))

print(f'Lista: {numeros}')
print(f'O maior valor digitado foi o {max(numeros)} na posição', end='')

maior_valor = max(numeros)
for pos, num in enumerate(numeros):
    if num == maior_valor:
        print(f' {pos+1} ', end='')

menor_valor = min(numeros)
print(f'\nO menor valor digitado foi o {min(numeros)} na posição', end='')
for pos, num in enumerate(numeros):
    if num == menor_valor:
        print(f' {pos+1} ', end='')

        