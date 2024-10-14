'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem 
ou não formar um triângulo.'''

# A soma de dois lados deve ser maior que o terceiro lado
print('-=-'*10,'\nTeste de triângulo\n','-=-'*10)

l1 = int(input('Escreva o primeiro lado: '))
l2 = int(input('Escreva o segundo lado: '))
l3 = int(input('Escreva o terceiro lado: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('É um triângulo')
else:
    print('Não é um triângulo')