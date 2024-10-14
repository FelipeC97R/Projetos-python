'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('Emprestimo de uma casa:\n','-'*30,'\n')
# valor_casa = float(input('Valor total da casa em reais: '))
# salario_comprador = float(input('Salário do comprador: '))
# total_anos_financiamento = int(input('Quantidade de anos a serem parcelados: '))
valor_casa = 100000
salario_comprador = 6000
total_anos_financiamento = 5 # 60 meses

total_meses_parcelamento = total_anos_financiamento * 12
parcela_mensal = valor_casa/total_meses_parcelamento

print(f'Para pagar uma casa que custa {valor_casa} em {total_anos_financiamento} anos, a parcela deve ser'
      f'\nde R${parcela_mensal:.2f}')

salario_comprar_imovel = parcela_mensal * 100/30

if parcela_mensal >= salario_comprador*30/100:
    print('Empréstimo negado: O valor do sálario do comprador está abaixo dos parâmetros.'
          f'\nO seu salário precisa chegar a no mínimo R${salario_comprar_imovel:.2f}')
else:
    print(f'Emprestimo aprovado')