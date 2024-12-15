'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome_jogador='não nomeado',gols=0):
    print('-'*20)
    print (f'\nFicha do jogador: ')
    print(f'{nome_jogador}')
    print(f'{gols}')
    print('-'*20)

nome = str(input('Digite o número do jogador: '))
gols = int(input('Numero de gols: '))

ficha(nome,gols)