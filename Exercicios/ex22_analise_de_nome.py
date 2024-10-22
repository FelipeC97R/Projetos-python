'''Realiza a analise de um name'''

from time import sleep
print('\n',f'{'ANALISADOR DE NOMES':-^30}')
while True:
    sleep(2)
    name =str(input('\nDigite o seu nome completo: '))

    print('Analisando nome ',end = '')
    sleep (1)
    for i in range (3):
        print(' .', end='', flush=True)
        sleep(1)
        
    print('\n','='*30)
    print(f'\nEm maiúscula: {name.upper()}\n'
        f'Em minúscula: {name.lower()}\n'
        f'Letras: {len(name)-name.count(' ')}\n'
        f'Espaços: {name.count(' ')}\n'
        f'Primeiro nome {name.split()[0]}\n'
        f'Letra no primeiro nome: {name.strip().find(' ')}')
    print('='*30)

    while True:
        chooseUserExit = input('Gostaria de testar outro nome?[s/n]:').upper()
        if chooseUserExit in ('S','N'):
            break
        print('Valor incorreto, tente novamente')
    if chooseUserExit == 'N':
        break