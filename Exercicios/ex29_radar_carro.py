'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
 A multa vai custar R$7,00 por cada Km acima do limite.'''

from math import ceil
vel_carro = float(input('\n Velocidade do carro: '))
if vel_carro > 80:
    print('O seu carro foi multado!')
    multa = ceil(vel_carro - 80)*7
    print(f'A multa será de {multa:.2f} R$')

print('\nTenha um bom dia e dirija com segurança.')