'''Converte valor dado em metros em cm e milímetros'''

print('\n',f'{'CONVERSÃO DE MEDIDAS':-^40}')

m = float(input('Coloque aqui o valor da distância em metros: '))
print(f'Valor em metros: {m:.2f} m\n'
      f'Valor em centímetros: {m*100:.2f}\n'
      f'Valor em milímetros: {m*1000:.2f}')
