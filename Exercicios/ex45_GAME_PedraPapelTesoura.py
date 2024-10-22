from random import randint
from time import sleep
print('-'*10,'\nRock, Paper, Scissors Game: \n','-'*10)
print('\nChoose some of the options bellow:\n[1] Rock\n[2] Paper\n[3] Scissors')
choiceIA = randint(0,2)

while True:
    choicePlayer = int(input('Choose: ')) -1
    if choicePlayer in(0,1,2):
        break
    print('Invalid option!,try again.')

print('Processando ',end='',flush=True)
sleep(1)
Options = ['Rock','Paper','Scissors']
if   0 <= choicePlayer < len(Options)+1:
    if Options[choiceIA] == Options[choicePlayer]:
        gameResult = 'DRAW'    
    elif (Options[choiceIA] == 'Rock'   and   Options[choicePlayer] == 'Paper'   or
        Options[choiceIA] == 'Paper'   and   Options[choicePlayer] == 'Scissors' or 
        Options[choiceIA] == 'Scissors' and   Options[choicePlayer] == 'Rock'):
        gameResult =  'PLAYER WIN'
    else:
    
        gameResult = 'PLAYER LOOSE'
    print(f'Escolha sua: {Options[choicePlayer]}')
    print(f'Escolha do computador: {Options[choiceIA]}')
    print(f'Resultado: {gameResult}')
else:
    print('Invalid Option!')


input('\nAcabou...')