'''Aprimore o desafio 93 para que ele funcione com vários jogadores,
 incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''


time = {}
while True:
    jogador = {}

    jogador['Nome'] = str(input('Nome jogador: '))
    jogador['Total_Partidas'] = int(input('Partidas jogadas: '))

    total_gols =0
    partida = []
    for p in range(jogador['Total_Partidas']) :
        partida.append(int(input(f'Gols na partida {p+1}: ')))

    jogador['GolsPorPartida'] = partida [:]
    jogador['Total_gols'] = sum(jogador['GolsPorPartida'])

    time.append(jogador.copy())

    while True:
        optionAddNewPlayers = str(input('Gostaria de adicionar mais jogadores?[s/n]').upper()[0])
        if optionAddNewPlayers in ('S','N'):
            break
        print('Valor invalido. Tente  "s" ou "n" ')

    if optionAddNewPlayers == 'N':
        break

print(f'{'Jogadores':^50}')
print('-'*50)
for jogador in time:
    print(f'{jogador['Nome']:<10}   Partidas: {jogador['Total_Partidas']:^6}  Gols: {jogador['Total_gols']:>6}')
print('-'*50)

while True:
    analise_jogador = str(input('Escolha um jogador para analizar (ou F para encerrar): ')).upper()
    if analise_jogador == 'F':
        break

    jogador_encontrado = False

    for jogador in time:
        if jogador['Nome'].upper() == analise_jogador:
            jogador_encontrado = True
            print('='*30)
            print(f'{jogador['Nome']:^30}')
            for jogo,gols in enumerate(jogador['GolsPorPartida']):
                print(f'{f'Jogo {jogo+1}:  {gols:>5} gols':^30}')
            print('='*30)
    if jogador_encontrado == False:
        print('Jogador não encontrado\n')