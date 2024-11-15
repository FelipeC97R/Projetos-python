'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

# grupo = [['Felipe',30.19],['Maria',67.88],['Carlos',78.2],['João',30.19]]

grupo = []
while True:
    pessoas = []
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    pessoas.append(nome)
    pessoas.append(peso)
    if len(grupo) == 0:
        maior_peso = menor_peso = pessoas[1]
    if pessoas[1] >= maior_peso:
        maior_peso = pessoas[1]
    elif pessoas [1]<= menor_peso:
        menor_peso = pessoas [1]
    grupo.append(pessoas[:])
    pessoas.clear()
    add_nome = input('Gostaria adicionar mais algum dado:').upper().strip()
    if add_nome == 'N':
        break

# max_weight = max(person[1] for person in groupWeight)
# min_weight = min(person[1] for person in groupWeight)

print(f'Total de pessoas cadastradas: {len(grupo)}')


print(f'\nPessoas com maiores pesos: {maior_peso} Kg')
for nome,peso in grupo:
    if peso == maior_peso:
        print(f' {nome}', end='')

print(f'\nPessoas com menores pesos: {menor_peso} Kg')
for nome,peso in grupo:
    if peso == menor_peso:
        print(f' {nome}', end='')