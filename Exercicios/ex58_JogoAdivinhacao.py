'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
print('-='*10,'\nJogo da adivinhação:\n','-='*10)
choiceUser = int(input('Escolha um número de 0 a 10:'))
choiceIA = randint(0,10)
attemptCount = 0
if choiceIA == choiceUser:
    print('Parabéns! voce acertou de primeira')
else :
    correct = False
    while not correct:
        if choiceIA < choiceUser:
            choiceUser = int(input('Você errou, era menor.Tente novamente: '))
        elif choiceIA > choiceUser :
            choiceUser = int(input('Você errou, era maior.Tente novamente: '))
        else: # choiceIA == choiceUser
            correct = True
        attemptCount += 1
    print(f'\nParabéns! Você acertou na {attemptCount} tentativa')

exit_program = input ("\n\nDigite qualquer tecla para sair...")