'''Faça um programa que tenha uma função chamada área(), que receba as
 dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno    .'''

def area(largura, comprimento):
    a = largura * comprimento
    print(f'Esse terreno tem {largura} X {comprimento} , o que dá {a} m²')

while True:
    largura = int(input('Largura: '))
    comprimento = int(input('Comprimento: '))
    area(largura,comprimento)