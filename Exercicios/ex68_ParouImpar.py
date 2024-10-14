'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o 
total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
counterVictories = 0
while True:
    while True:
        playerEvenOddOption = input('Escolha par ou impar [P/I]: ').lower().strip()
        if playerEvenOddOption in ('p','i'):
            break
        print('Valor digitado incorreto. Tente novamente\n')
    if playerEvenOddOption == 'p':
        playerEvenOddOption = 'even'
    else:
        playerEvenOddOption ='odd'

    playerTurn = int(input('De um valor: '))
    iaTurn = randint(0,10)
    sumOfTurns = playerTurn + iaTurn
    print(f'O computador jogou {iaTurn}.\nA soma deu {sumOfTurns}')
    if sumOfTurns % 2 == 0: 
        gameResult = 'even'
    else:
        gameResult = 'odd'
    if playerEvenOddOption != gameResult:
        print('\nInfelizmente não foi dessa vez.')
        break
    else:
        print(f'Parabéns! Você venceu... \nVamos para a {counterVictories + 2} rodada')
    counterVictories +=1
print(f'Voce teve um total de {counterVictories} vitórias')