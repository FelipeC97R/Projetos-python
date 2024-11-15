'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
 entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
mega = []
total_jogos = int(input('Quantos jogos você gostaria de fazer?'))
for i in range (total_jogos):
    jogo = []
    for i in range(6):
        while True:
            numero = randint(1,60)   
            if numero not in jogo:
                jogo.append(numero)
                break
    mega.append(jogo[:])

for j in mega:
    print(j)