'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
q_tinta = float(input('Quantos metros quadrados a tinta pinta: '))

tinta = largura *altura /q_tinta

print(f'A quantidade de tinta necessária é de {tinta} litros.')