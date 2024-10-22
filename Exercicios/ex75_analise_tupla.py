'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

userNumbers = (int(input('Digite o primeiro número: ')),
               int(input('Digite o segundo número: ')),
               int(input('Digite o terceiro número: ')),
               int(input('Digite o quarto número: ')))

print(f'A lista de números: {userNumbers}')
print(f'Quantas vezes apareceu 9: {userNumbers.count(9)}')
if 3 in userNumbers:
    print(f'Em que posição apareceu o valor 3: {userNumbers.index(3)+1}')
else:
    print('O valor 3 não apareceu na tupla')
count = 0
for num in userNumbers:
    if num % 2 == 0:
        count +=1

print(f'O total de números pares é : {count}')