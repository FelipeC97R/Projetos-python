''' mostra os primeiros termos da progressão usando a estrutura while, perguntando para o usuário quantos mais termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.'''

from time import sleep
while True:
    initialValue = int (input('Digite a primeiro valor da PA:'))
    paRatio = int(input('Digite a razão da PA: '))
    numberElements = int(input('Qual o total de elementos: '))

    print('-'*30,f'\n{f'PA de razão {paRatio} iniciando em {initialValue}':^30}\n','-'*30)
    position = 0
    
    first_loop = True
    while True:
        if first_loop == False:
            extra_terms= int(input('\nMais quantos termos gostaria de adicionar? '))
            position = numberElements
            numberElements += extra_terms

        while position < numberElements:
            elementNPosition = initialValue + paRatio * position 
            print(f'{elementNPosition}', end = '',flush=True)
            sleep(0.1)
            print(' , ' if position < numberElements -1 else '',end='')
            position += 1
        
        while True:
            option_exit = input('Gostaria de sair [s/n]:').upper().strip()
            if option_exit in ('S','N'):
                break
            print('opção inválida')

        if option_exit == 'S':
            break

        first_loop = False
    