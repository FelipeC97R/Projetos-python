''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%.'''

sal = float(input('Digite aqui o valor do seu salário em reais: '))

if sal > 1250:
    aum_sal = 0.1
else:
    aum_sal = 0.15

print(f'O seu salário final será {sal+(sal*aum_sal):.2f}R$') 