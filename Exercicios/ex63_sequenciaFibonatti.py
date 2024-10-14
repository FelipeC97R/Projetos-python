'''Escreva um programa que leia um número N inteiro qualquer e 
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.'''

total_termos = int(input('Quantos termos você quer ver da sequencia Fibonecci: '))

termo_anterior = 0
termo = 1
contador = 0
while contador < total_termos:
    proximo_termo = termo + termo_anterior
    print(proximo_termo)
    termo_anterior = termo
    termo = proximo_termo
    contador += 1
    