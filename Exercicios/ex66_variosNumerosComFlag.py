'''Crie um programa que leia números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, 
 que é a condição de parada. No final, mostre quantos números 
 foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''


sumNumbers = counter = 0 
while True:
    number = int(input('Digite um número [-1 para sair]: '))
    if number == -1:
        break
    sumNumbers += number
    counter += 1

print(f'Soma : {sumNumbers}')
print(f'Total de números : {counter}')