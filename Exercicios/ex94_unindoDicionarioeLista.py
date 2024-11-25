'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
 No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D)
   Uma lista de pessoas com idade acima da média'''

bancoDadosGrupo = []
while True:
  pessoa = {}

  pessoa['nome'] = str(input('Nome: '))

  while True:
      pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
      if pessoa['sexo'] in ('M','F'):
          break

  pessoa['idade'] = int(input('Idade: '))
  
  bancoDadosGrupo.append(pessoa.copy())

  while True:
    option_exit = str(input('Gostaria de encerrar?[s/n]')).upper()[0]
    if option_exit in ('S','N'):
      break
    
  if option_exit == 'S':
     break



print(f'\nTotal de pessoas cadastradas: {len(bancoDadosGrupo)}')

soma_idades = sum(pessoa['idade']for pessoa in bancoDadosGrupo)
media_idades = soma_idades / len(bancoDadosGrupo)
print(f'Media das idades: {media_idades:.2f}\n')

print('Pessoas com idade acima da média: ')    
for pessoa in bancoDadosGrupo:
  if pessoa['idade']>= media_idades:
    print(f'{pessoa['nome']} com idade {pessoa['idade']}')

print('\nMulheres do grupo:')
for pessoa in bancoDadosGrupo:
  if pessoa['sexo'] == 'F':
      print(pessoa['nome'])