'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
 só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''


def leiaInt(conteudo):
    while True:    
        aux = str(input(conteudo))
        if aux.isnumeric():
            break
        else:
            print('\033[0;31;40m Erro! Não é um número\033[m')
    print(aux) 

leiaInt('Digite um número: ')