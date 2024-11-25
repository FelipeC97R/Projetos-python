'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. '''

while True:

    number = float(input('Digite um número qualquer: '))
    doubleNumber = number * 2
    tripleNumber = number * 3 
    squareRootNumber = number ** (1/2)

    print(f'Número: {number}'
          f'\nSeu dobro: {doubleNumber}'
          f'\nSeu Triplo: {tripleNumber}'
          f'\nSua Raíz quadrada: {squareRootNumber:.2f}')


    option_quit = str(input('Gostaria de sair[s/n]: ')).upper().strip()
    if option_quit == 'S':
        break