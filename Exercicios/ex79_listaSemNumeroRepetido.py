'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''


# numeros = [8,20,16,7]
numeros = []

while True:
    
    valor = int(input('Digite um número: '))
    if valor not in numeros:
        numeros.append(valor)
    else:
        print('Valor duplicado, não vou adicionar')

    while True:
        inserirValor = input('Gostaria de acrescentar mais um número a lista?[s/n]:').upper()
        if inserirValor in ('SN'):
            break
        print('Valor digitado inválido , tente "s" ou "n"')
    if inserirValor == 'N':
        break

print(f'Lista: {sorted(numeros)}')