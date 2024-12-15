'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento 
de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(birthYear=0):
    from datetime import datetime
    
    age = datetime.now().year - birthYear
    if age < 16:
        return print('NEGADO')
    elif 16 <= age < 18 or age >= 65:
        return print('OPCIONAL')
    else:
        return print('OBRIGATÓRIO')

data_nascimento = int(input('Digite o seu ano de nascimento: '))

voto(data_nascimento)
