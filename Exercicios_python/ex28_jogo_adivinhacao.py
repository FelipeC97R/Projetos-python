'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para 
o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
num_usuario = float(input('Digite um número inteiro entre 0 e 5: '))
num_rand = randint(0,5)
print('-=-'*20)
print('Processando', end='')
sleep(1)
print(' .', end = '')
sleep(1)
print(' .', end = '')
sleep(1)
print(' .', end = '')
sleep(1)
if num_usuario >= 0 and num_usuario <=5:  # O número está dentro do intervalo de 0 a 5?
    if num_usuario.is_integer() == True: # É um número inteiro?
        print(f'\n O número aleatório: {num_rand}\n')
        if num_usuario == num_rand: # Usuário acertou o número?
            print('Parabéns, você acertou!!!')
        else:
            print(f'Que pena você errou. O seu número era {num_usuario}')
    else:
        print('Erro! O número digitado não é inteiro')
else:
    print('Erro! O número digitado não estava entre 0 e 5')