'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
 início, fim e passo. Seu programa tem que realizar três contagens através da função criada
 
 a) de 1 até 10, de 1 em 1
 b) de 10 até 0, de 2 em 2
 c) uma contagem personalizada'''

from time import sleep
def contador(customStart,customEnd,customStep):
    for number_iteration in range (3):
        if number_iteration == 0:
            start_local = 1
            end_local = 11
            step_local = 1
        elif number_iteration == 1:
            start_local = 10
            end_local = -1
            step_local = -2
        else:
            start_local = customStart
            end_local = customEnd 
            step_local = customStep

        for numberValue in range (start_local,end_local,step_local):
            print(f'{numberValue} ',end= '', flush=True)
            sleep(0.1)
        print()

start = int(input('Inicio: '))
end = int(input('Fim: '))
step = int(input('Passo: '))

contador(start,end,step)