'''Crie um programa que tenha uma tupla única com nomes 
de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

produtos_precos = (
    ("Arroz", 20.50),
    ("Feijão", 7.30),
    ("Macarrão", 4.80),
    ("Leite", 5.00),
    ("Azeite", 15.75),
    ("Açúcar", 3.90)
)

print('-'*40)
print(f'{'LISTA DE PREÇOS':^40}')
print('-'*40)
# Exemplo de como exibir os produtos e preços:
for produto, preco in produtos_precos:
    print(f'{f"{produto:.<25}R${preco:>7.2f}":^40}')
