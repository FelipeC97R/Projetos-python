km = int (input('Digite quantos quilômetro foram percorridos: '))
dias = float(input('Digite quantos dias foi alugado: '))

v_aluguel  = km * 0.15 + (dias *60)
print(f'O valor gasto foi de {v_aluguel}')
