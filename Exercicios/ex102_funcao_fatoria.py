'''Crie um programa que tenha uma função number_fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um 
valor lógico (opcional) indicando se será mostrado ou não na tela o processo 
de cálculo do fatorial.
'''


def fatorial(number_fatorial, show = False):

    """
    Calculate the factorial of a number
    
    Args: 
        number_fatorial (int) : The interger for which the factorial will be calculate
        show(bool): Indicate whether to display the calculation process (defalt is False)
    """
    from time import sleep

    factorial_result = 1
    for i in range(number_fatorial,0,-1):
        factorial_result *= i

    if show == True:
        print(f'Process to calculate the factorial of {number_fatorial}:')
        for i in range(number_fatorial,0,-1):
            print(f'{i} = ' if i == 1 else f'{i} X ',end='', flush= True )
            sleep(0.3)

    print(f'{factorial_result:,}')

fat = int(input('Digite um valor para encontrar o fatorial: '))


help(fatorial)


