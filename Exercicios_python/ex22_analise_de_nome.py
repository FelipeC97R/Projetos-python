

nome =str(input('Digite o seu nome completo: '))

print(f'{nome}\n'
      f'Em maiúscula: {nome.upper()}\n'
      f'Em minúscula: {nome.lower()}\n'
      f'Letras: {len(nome)-nome.count(' ')}\n'
      f'Espaços: {nome.count(' ')}\n'
      f'Primeiro nome {nome.split()[0]}\n'
      f'Letra no primeiro nome: {nome.strip().find(' ')}')