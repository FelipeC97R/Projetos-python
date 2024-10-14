''' Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.'''

from time import sleep
print('-='*5,'GERADOR DE TABOADA','-='*5,'\n')
while True:
    tableNumber = int(input('Quer ver a taboada de qual valor? '))
    if tableNumber < 0 :
        break
    tableLimit = int(input('Qual será o número final da taboada: '))

    print('\n','*'*5 ,f'Taboada do {tableNumber}','*'*5,'\n')
    sleep (1)
    for i in range (1,tableLimit):
        print(f'{tableNumber} X {i:<2} = {tableNumber*i}') 
        sleep(0.2)

input('Fim do programa. Digite enter para finalizar...')