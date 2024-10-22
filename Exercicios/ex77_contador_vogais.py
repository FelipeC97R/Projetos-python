'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
 Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

wordCollection = ("livro", "computador", "mesa", "café", "janela", "telefone", "carro", "flor", "relógio", "cadeira")
teste = 'livro'
for word in wordCollection:
    print(f'{word}: ',end='')
    for letter in word:
        print (f'{letter}' if letter in ('aeiou') else ' ', end='')
    print('')