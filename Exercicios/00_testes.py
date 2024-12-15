'''Faça uma função que leia três números e mostre qual é o maior e qual é o menor.'''

def ler_numeros(arg_num1,arg_num2,arg_num3):
    maior = arg_num1
    menor = arg_num1

    if arg_num2 >= arg_num1:
        maior =  arg_num2
        if arg_num3 >= arg_num2:
            maior = arg_num3
    if arg_num2 <= arg_num1:
        menor =  arg_num2
        if arg_num3 <= arg_num2:
            menor = arg_num3
    print (f'{maior},{menor}')


ler_numeros(4,5,6)

max