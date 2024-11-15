'''Crie um programa que declare uma matriz de dimensão 3×3 e
 preencha com valores lidos pelo teclado.
 No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[],[],[]]
print('Digite os valores das coordenadas: \n')
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'({i+1},{j+1}): ')))
        

for linha in matriz:
    for coluna in linha:
        print(f'{coluna:^5}',end ='')
    print('')