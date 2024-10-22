lista_compras = (('Pepino',45.99),('Cebola',27.50),('Batata frita',5.99))

for produto,preco in lista_compras:
    print(f'{produto:.<25}R${preco:>7}')