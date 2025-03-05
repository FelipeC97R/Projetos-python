import moeda

money = int(input('Digite o seu dinheiro em reais: '))
print(f'O valor inicial: {moeda.transformaReais(money)}')
print(f'O dobro disso é {moeda.dobro(money,True)}')
print(f'Aumentando 18% temos: {moeda.aumentar(money,18,True)}')
