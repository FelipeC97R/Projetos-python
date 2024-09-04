'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: 
 O primeiro valor é maior
 O segundo valor é maior
 Não existe valor maior, os dois são iguais'''

first_number = int(input('Digite o primeiro número: '))
second_number = int(input('Digite o segundo número: '))


if first_number > second_number:
    highest_number = first_number
    lowest_number = second_number
elif first_number < second_number:
    highest_number = second_number
    lowest_number = first_number
else: 
    print(f'Os números {first_number} e {second_number} são iguais')

print(f'O maior número é {highest_number} e o menor número é {lowest_number}')