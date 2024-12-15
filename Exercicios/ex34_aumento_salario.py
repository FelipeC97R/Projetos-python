''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
o aumento é de 15%.'''

employee = {}
employee['nome'] = str(input('Nome:'))
employee['salario'] = int(input(f'Valor salário de {employee["nome"]}: '))

if employee ['salario'] > 1250:
    employee ['condicao'] = 'aumento 10%'
    employee['salario'] *= 1.1
else:
    employee ['condicao'] = 'aumento 15%'
    employee['salario'] *= 1.15

print(employee)