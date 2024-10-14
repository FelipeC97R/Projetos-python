'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:'''

frase = str(input('Digite uma frase:')).strip().upper()
noSpaceFrase= ''.join(frase.split())
invertedFrase = noSpaceFrase[::-1]
#invertedFrase = ''
# for letter in range (len(frase)-1,-1,-1):

#     invertedFrase += frase[letter]
 
if invertedFrase == noSpaceFrase:
    print('é um palindromo')
else:
    print('Não é um palíndromo')

