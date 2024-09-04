'''Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

integerValue = int(input('Digite aqui um número inteiro: '))

print('-'*20,'\nMenu de opções:\n'
      '[1] Converter para binário\n'
      '[2] Converter para octal\n'
      '[3] Converter para hexadecimal\n',
      '-'*20)
option_binary = 1
option_octal = 2
option_hexadecimal = 3

conversion_choice = int(input('Escolha uma das opções: '))
print('\n')
if conversion_choice == option_binary:
    result_conversion = bin(integerValue)
    print(f'O resultado em binário é {result_conversion[2:]}')
elif conversion_choice == option_octal:
    result_conversion = oct(integerValue)
    print(f'O resultado em octal é {result_conversion[2:]}')
elif conversion_choice == option_hexadecimal:
    result_conversion = hex(integerValue)
    print(f'O resultado em hexadecimal é {result_conversion[2:]}')
else:
    print('Valor digitado inválido!')

