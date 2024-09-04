num = int(input('Digite um número de 0 a 9999: '))
print(f'Número: {num}\n'
      f'Unidade: {num%10}\n'
      f'Dezena: {num%100//10}\n'
      f'Centena: {num//100%10}\n'
      f'Milhar: {num // 1000}')