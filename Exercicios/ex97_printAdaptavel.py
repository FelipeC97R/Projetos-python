'''Faça um programa que tenha uma função chamada escreva(),
 que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def titulo (texto):

    tam_subl = len(texto) + 10
    print('-'*(tam_subl))
    print(f'{texto:^{tam_subl}}')
    print('-'*(tam_subl))

titulo(input('Digite um texto qualquer: '))