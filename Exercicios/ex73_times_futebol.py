'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

brazilian_teams = (
    "Flamengo",
    "Palmeiras",
    "São Paulo",
    "Santos",
    "Corinthians",
    "Vasco da Gama",
    "Atlético Mineiro",
    "Fluminense",
    "Internacional",
    "Grêmio",
    "Botafogo",
    "Cruzeiro",
    "Chapecoense",
    "Bahia",
    "Ceará",
    "Fortaleza",
    "Coritiba",
    "Goiás",
    "Atlético Goianiense",
    "Sport Recife"
)

print('Times em ordem alfabética: ')
for i in sorted(brazilian_teams):
    print(i)

print('\n Os 5 primeiros colocados: ')
for team in brazilian_teams[0:5]:
    print(f'{brazilian_teams.index(team)+1}º: {team}')

print('\nOs 4 ultimos colocados: ')
for team in brazilian_teams[-4:]:
    print(f'{brazilian_teams.index(team)+1}º: {team}')


print(f'Em que posição está o Chapecoense: {brazilian_teams.index('Chapecoense')}')
