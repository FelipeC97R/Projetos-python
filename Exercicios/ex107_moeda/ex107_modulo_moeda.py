import moeda

money = int(input('Digite o seu dinheiro em reais: '))
print(f'O dobro disso é {moeda.dobro(money)}')
print(f'Aumentando 18% temos: {moeda.aumentar(money,18)}')