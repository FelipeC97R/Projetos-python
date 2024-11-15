''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Ameixa','Batata','Laranja')

for p in palavras:
    print('Vogais:',end='')
    for letra in p:
       if letra.lower() in ('aeiou'):
        print(f'{letra} ',end='')
    print()