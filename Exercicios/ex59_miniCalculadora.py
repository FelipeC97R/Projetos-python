'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa'''

from time import sleep

print('-='*10,'Calculadora','-='*10,'\n')
firstNumber = int(input('Primeiro número: '))
secondNumber = int(input('Segundo número: '))
chooseUser = 0
while chooseUser != 5:
    
    print('[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] mostrar maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa\n')
    chooseUser = int(input('Escolha uma das opções acima:'))
    
    if chooseUser == 1:
        result_operation = firstNumber + secondNumber
        print(f'A soma é {result_operation}')
    elif chooseUser == 2:
        result_operation = firstNumber * secondNumber
        print(f'A multiplicação é {result_operation}')
    elif chooseUser == 3:
        if secondNumber > firstNumber:
            result_operation = secondNumber
        else: # firstNumber > secondNumber
            result_operation = firstNumber
        print(f'O maior número é {result_operation}')
    elif chooseUser == 4:
        firstNumber = int(input('Primeiro número: '))
        secondNumber = int(input('Segundo número: '))
        print('\n Retornando ao menu ...')
    sleep(2)    
