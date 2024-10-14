'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
 mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
   O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''



soma = 0
contador = 0
decisao = ' '
while decisao not in 'N' :
    numero  = int(input('Digite um número inteiro: '))
    soma += numero
    if contador == 0:
        maiorNumero = menorNumero = numero
    elif numero < menorNumero:
        menorNumero = numero
    elif numero > maiorNumero:
        maiorNumero = numero
    contador += 1
    decisao = str(input('Deseja continuar digitando valores? (S/N)')).upper().strip()

media = soma / contador

print(f'Total de números: {contador}')
print(f'Maior número: {maiorNumero}')
print(f'Menor número: {menorNumero}')
print(f'Soma: {soma}')
print(f'Média: {media:.2f}')
