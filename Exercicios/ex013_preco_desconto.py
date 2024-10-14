'''Faça um algoritmo que leia o preço de um produto e 
mostre seu novo preço, com 5% de desconto.'''
preco_produto = float(input('Digite o valor do produto: '))
preco_desconto = preco_produto * 0.95
print(f'O valor com desconto é  {preco_desconto:.2f}')