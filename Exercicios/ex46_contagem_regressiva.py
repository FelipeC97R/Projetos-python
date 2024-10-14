'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep

print('*'*5,'Contagem de Ano Novo','*'*5,'\n')
for countdown in range(10,-1,-1):
    sleep(1)
    print ('\r',' '*11,f'{countdown:2}', end = '',flush = True)

sleep (1)
print ('\r',' '*5,'Happy new year!!!')
sleep(2)

input('\nDigite qualquer tecla para sair ...')