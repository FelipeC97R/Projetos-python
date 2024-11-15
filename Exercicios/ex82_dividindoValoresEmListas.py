'''Crie um programa que vai ler vários números e colocar em uma lista.
 Depois disso, crie duas listas extras que vão conter apenas os valores pares
   e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

mainNumberList = [1,2,4,52,3,5,7,9,8,11]

# while True:
#     mainNumberList.append(int(input('Digite um número: ')))

#     addMoreNumbers = input('Gostaria de adicionar outro valor?[s/n]: ').lower().strip()
#     if addMoreNumbers == 'n':
#         break

evenList = []
oddList = []
for num in mainNumberList:
    if num % 2 == 0:
        evenList.append(num)
    else:
        oddList.append(num)

print(f'Lista padrão: {mainNumberList}')
print(f'Lista numeros pares: {evenList}')
print(f'Lista números impares: {oddList}')