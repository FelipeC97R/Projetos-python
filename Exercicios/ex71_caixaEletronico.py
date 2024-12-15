'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

from time import sleep
print('-'*30,'\n',f'{"BANCO ABUDABIS":^30}','\n', '-'*30)
sleep(1)

totalAmountMoney = int(input('Quanto será o valor sacado: '))
Bills = [50,20,10,1]

for bill in Bills:
    countBills = 0
    while totalAmountMoney >= bill:
        totalAmountMoney -= bill
        countBills +=1
    sleep(1)
    print(f'Notas de {bill}: {countBills}')

print('Imprimindo notas ...')
sleep(2)
print('\nImpressão concluida. Volte Sempre!')

input('Digite enter para sair...')