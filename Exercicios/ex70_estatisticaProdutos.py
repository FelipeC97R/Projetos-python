'''Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

from time import sleep
print('+'*10, 'Leitor de compras', '+'*10)
print('-'*30,'\nMERCADO THORIN\n','-'*30,)

purchaseTotal = lessPrice = counterTotalProducts=counterProcuctsMoreThan1000 = 0
while True:
    productName = input('Digite o nome do produto: ')
    productPrice = float(input('Digite o preço do produto em [R$]'))
    while True:
        userWantsToProceed = input('Deseja continuar adicionando produtos: ').upper().strip()
        if userWantsToProceed in ('SN'):
            break
        print('Valor inválido, tente novamente')
    counterTotalProducts += 1
    purchaseTotal += productPrice    
    
    if counterTotalProducts == 1 or productPrice < lessPrice:
        lessPriceProductName = productName
        lessPrice = productPrice
        
    if productPrice > 1000:
        counterProcuctsMoreThan1000 += 1

    if userWantsToProceed == 'N':
        print('Finalizando compra...')
        sleep(2)
        break
    
print('-'*30,'\nFIM DO PROGRAMA\n','-'*30,)
print(f'Valor total da compra : {purchaseTotal:.2f} R$'
      f'\nProduto mais barato: {lessPriceProductName} R$ , valor: {lessPrice:.2f} R$'
      f'\nTotal de produtos que valem mais de 1000 {counterProcuctsMoreThan1000}')