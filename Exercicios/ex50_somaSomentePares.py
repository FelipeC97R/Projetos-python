'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
evenSum = 0
evenCount = 0
for i in range (1,7):
    numberUser = int(input(f'Digite {i}º número: '))
    if numberUser % 2 == 0:
        evenSum += numberUser
        evenCount += 1

print (f'Foram contados {evenCount} números pares.\nA soma total é de {evenSum}')