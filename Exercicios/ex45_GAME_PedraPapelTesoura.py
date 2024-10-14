from random import randint

print('-'*10,'\nRock, Paper, Scissors Game: \n','-'*10)
print('\nChoose some of the options bellow:\n[1] Rock\n[2] Paper\n[3] Scissors')
choiceIA = randint(0,2)
choicePlayer = int(input('Escolha: ')) -1

# Verification of INPUTS
# choiceIA = 2 
# choicePlayer = 4

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