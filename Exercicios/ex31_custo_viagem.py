'''Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
e R$0,45 parta viagens mais longas.'''

dist_viagem = float(input('Olá, bem vindo ao simulador de viagens.\nDigite a distância total' 
                          'pretendida em sua viagem [km]:  '))

if dist_viagem <= 200:
    valor_viagem = dist_viagem * 0.5
else:
    valor_viagem = dist_viagem *0.45

print(f'O total gasto na viagem será de {valor_viagem:.2f} R$')