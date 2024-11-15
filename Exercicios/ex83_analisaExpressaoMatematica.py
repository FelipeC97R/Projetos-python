'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
 Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

# expressao = input('Digite uma expressão matemática: ')
expressao = '(54+2)/2)+(34*3))'
if '(' in expressao:
    counter_open = 0
    counter_close = 0
    for i in expressao:
        if i == '(':
            counter_open +=1
        elif i == ')':
            counter_close +=1
    if counter_close > counter_open:
        print('Expressão com parênteses faltando')
        

# outra forma 
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
