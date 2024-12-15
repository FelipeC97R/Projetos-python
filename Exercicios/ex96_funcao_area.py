'''Faça um programa que tenha uma função chamada área(), que receba as
 dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno    .'''

def area(largura, comprimento):
    """
    Esta função recebe a largura e comprimento e retorna a area  
    Arguments:
        largura (float) : Medida de distância do objeto a ser medido
        comprimento (float): Medida do comprimento do objeto a ser medido

    Return: 
        area(float) : Resultado do calculo da área 
    """
    a = largura * comprimento
    print(f'Esse terreno tem {largura} X {comprimento} , o que dá {a} m²')

help (area)
while True:
    largura = int(input('Largura: '))
    comprimento = int(input('Comprimento: '))
    area(largura,comprimento)

