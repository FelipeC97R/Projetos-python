'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação 
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(conteudo):
    while True:
        try:
            num = int(input(conteudo))
        except ValueError:
            print('O valor digitado não é um número')
            continue
        return num


def leiaFloat(conteudo):
    while True:
        try:
            num = float(input(conteudo))
        except ValueError:
            print('O valor digitado não é um número')
            continue
        else:
            return num


leiaFloat('Digite um número inteiro: ')