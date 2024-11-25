'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o 
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
 o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
   além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

banco_dados = []
while True:
    trabalhador = {}
    trabalhador['nome'] = str(input('Nome: '))
    ano_nascimentoTrab = int(input('Ano de nascimento: '))
    trabalhador['idade'] = datetime.now().year - ano_nascimentoTrab
    trabalhador['nCarteiraTrabalho'] = int(input('Nº Carteira de Trabalho: '))

    if trabalhador['nCarteiraTrabalho'] != 0:
        trabalhador['ano_contratacao'] = int(input('Ano contratação: '))
        trabalhador['salario'] = str(input('Salário: '))
        trabalhador['aposentadoria'] = trabalhador['ano_contratacao']+35 - datetime.now().year
    banco_dados.append(trabalhador.copy())

    while True:
        optionQuit = input('Gostaria de finalizar[s/n]').lower().strip()
        if optionQuit in 'sn':
            break
        print('Valor inválido ')
    if optionQuit == 's':
        break

for trabalhador in banco_dados:
    print('')
    for categoria, dados in trabalhador.items():
        print(f'{categoria}: {dados}')