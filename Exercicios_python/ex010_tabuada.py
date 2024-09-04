nome = input('Digite o nome do aluno: ')
num1 = int(input(f'Digite a primeira nota de {nome}: '))
num2 = int(input(f'Digite a segunda nota de {nome}: '))

med = (num1+num2)/2
print(f'A média de {nome} é {med:.1f}')