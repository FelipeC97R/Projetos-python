'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
 No final do programa, mostre: a média de idade do grupo,
   qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaIdades = 0 
maiorIdade = 0
contadorMulheresMenos20 = 0
nomeHomemMaisVelho = ''
for i in range (0,1):
    print('-'*5,f'{i+1}º Pessoa','-'*5)
    nome = str(input(f'Nome:'))
    sexo = str(input(f'Sexo:'))
    idade = int(input(f'Idade:'))
    somaIdades += idade
    if idade > maiorIdade and sexo.upper().strip() == 'M':
        nomeHomemMaisVelho = nome
    
    if idade < 20 and sexo.upper().strip() == 'F':
            contadorMulheresMenos20 += 1     
            print (contadorMulheresMenos20)

mediaIdades = somaIdades / 4
print()
print('-'*5,'Resultados','-'*5)
print(f'Média das idades = {mediaIdades:.2f}\n'
      f'Nome do homem mais velho: {nomeHomemMaisVelho}\n'
      f'Total de mulheres com menos de 20: {contadorMulheresMenos20}\n')