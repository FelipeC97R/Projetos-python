'''Mostra o quanto de dinheiro temos na carteira e mostra
o valor em dolar'''

dinReal= float(input('Digite a quantidade de dinheiro no banco: '))
convDolarReal = 5 # O quanto vale 1 dolar convertendo em real
dinDolar = dinReal/convDolarReal # Uma simples regra de 3 do valor de dolar e real

print(f'O valor de {dinReal:.2f} reais equivaler a ${dinDolar:.2f} dólares')
