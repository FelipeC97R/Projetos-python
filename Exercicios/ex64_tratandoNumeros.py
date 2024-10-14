'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 0, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

numero = 1
soma = 0
contador = 0
while numero != 0:
    numero = int(input('Digite um número qualquer [digite 0 para sair]: '))
    soma += numero
    contador += 1

print(f'O foram no total de {contador} números somados que resultaram na soma igual a {soma}')