'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou.
 Depois vai ler a quantidade de gols feitos em cada partida. 
 No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''


jogador = {}

jogador['Nome'] = str(input('Nome jogador: '))
jogador['Total_Partidas'] = int(input('Partidas jogadas: '))

total_gols =0
partida = []
for p in range(jogador['Total_Partidas']) :
    partida.append(int(input(f'Gols na partida {p+1}: ')))

jogador['GolsPorPartida'] = partida [:]
jogador['Total_gols'] = sum(jogador['GolsPorPartida'])
print(jogador)