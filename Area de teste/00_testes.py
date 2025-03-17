'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.(melhorar ex 47)'''

idades = list()

for i in range (7):
    idades.append(int(input(f'Digite a idade da pessoa {i+1}: ')))

totalMaior18 = len(list(filter(lambda idade_pessoa : idade_pessoa>18, idades)))
print(idades)
print(f'O total de pessoas maior de 18 é {totalMaior18}')