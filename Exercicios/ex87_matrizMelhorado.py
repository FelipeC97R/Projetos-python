'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[],[],[]]
print('Digite os valores das coordenadas: \n')

somaPares = somaTerceiraColuna = 0
for i in range(3):
    for j in range(3):
        coordenada = int(input(f'({i+1},{j+1}): '))
        matriz[i].append(coordenada)
        if matriz[i][j] % 2== 0:
            somaPares += coordenada
        if j == 2:
            somaTerceiraColuna += coordenada
        if j == 1:
            if i == 0:
                maiorValorSegundaColuna = matriz[i][j]
            if matriz[i][j]>= maiorValorSegundaColuna:
                maiorValorSegundaColuna = matriz[i][j]

for linha in matriz:
    for coluna in linha:
        print(f'{coluna:^5}',end ='')
    print('')

print(f'A soma dos pares: {somaPares}')
print(f'Soma terceira coluna: {somaTerceiraColuna}')
print(f'Maior valor da segunda coluna: {maiorValorSegundaColuna}')