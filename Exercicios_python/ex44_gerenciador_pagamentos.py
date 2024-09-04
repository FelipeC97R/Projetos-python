print('\n'*2,'Sistema de controle de pagamentos\n','-'*40,'\n')
groceryTotal = float(input('Qual foi o valor total da compra [R$]: '))

print('Formas de pagamento:\n[1]- À vista em dinheiro\n[2]- À vista no cartão\n[3]- No cartão em 2X vezes\n[4]- 3X ou mais')
paymentOption = int(input('Opção escolhida: '))
optionProblem = 999
interestValue = 0
discountValue = 0
numberInstallments = 1
if paymentOption == 1:
    discountValue = 0.1
elif paymentOption == 2:
    discountValue = 0.05
elif paymentOption == 3:
    discountValue == 0 
    numberInstallments = 2
elif paymentOption == 4:
    interestValue = 0.2
    numberInstallments = int(input('Total de parcelas: '))
else:
    print ('Escolha de pagamento inválida!')
    paymentOption = optionProblem
totalDiscount = groceryTotal * discountValue
totalInterest = groceryTotal * interestValue
totalFinalPayment = groceryTotal * (1 - discountValue + interestValue)
paymentoForEachInstallment = totalFinalPayment /numberInstallments 
if paymentOption != optionProblem:
    print(f'Total do desconto: {totalDiscount:.2f} R$')
    print(f'Total de parcelas: {numberInstallments}')
    print(f'Valor a ser pago em cada parcela: {paymentoForEachInstallment:.2f} R$')
    print(f'Total em juros: {totalInterest:.2f} R$')
    print(f'Valor final: {totalFinalPayment:.2f} R$')