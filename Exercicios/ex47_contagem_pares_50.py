'''Um programa que mostra na tela todos os números pares que estão dentro de um intervalo'''

from time import sleep
print('-'*30,f'\n{'Números pares':^30}\n','-'*30)
sleep(1)
print('\nEscolha o intevalo que deseja ver de números pares')
sleep(1)

evenMinInterval = int(input('Digite o menor valor intervalo: ')) 
evenMaxInterval = int(input('Digite o maior valor intervalo: ')) 
if evenMinInterval > evenMaxInterval:
    auxVar = evenMaxInterval
    evenMaxInterval = evenMinInterval
    evenMinInterval = auxVar
    print('Trocamos a ordem pois o menos valor está no lugar do maior valor')
if evenMinInterval %2 == 1:
    evenMinInterval +=1
sleep(1)
print('Os números pares dentro desse intervalo são: ',end='')
for i in range (evenMinInterval,evenMaxInterval,2):
    print(f'{i} ',end='',flush=True)
    sleep(0.1)