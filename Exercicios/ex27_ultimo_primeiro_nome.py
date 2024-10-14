nome = str(input('Digite o seu nome completo: ')).strip()
'''Forma 1
    print(f'O seu primeiro nome é : {nome[:nome.find(' ')]}\n'
      f'O seu último nome é: {nome[nome.rfind(' ')+1:]}') '''

print(f'O seu primeiro nome é : {nome.split()[0]}\n'
      f'O seu ultimo nome é: {nome.split()[len(nome.split())-1]} ')
