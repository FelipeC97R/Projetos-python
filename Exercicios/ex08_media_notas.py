'''Um programa que lê o nome do aluno, a matéria e as duas notas que foi nas provas,
calcula e mostra a sua média.'''

import time
#leitura de variáveis nome,matéria da prova e notas
nome = str(input('Qual é o nome do aluno: '))
materia =str(input('Nome da matéria: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
if n1 <0:
    print('O a primeira nota é invalida, será considerada como zero no calculo.')
    n1 = 0
if n2 <0:
    print('O a segunda nota é invalida, será considerada como zero no calculo.')
    n2 = 0
#Timer de processamento
print('Calculando ',end='')
for i in range (3):
    print('. ',end='',flush=True)
    time.sleep(1)

# calcula a média aritmética das duas notas
med = (n1 + n2)/2 
print('\n','-'*20,f'Aluno: {nome}\n'
      f'Matéria: {materia}\n'
      f'Média: {med}\n')
if med < 7: # Verifica se aluno foi aprovado
    print(f'O aluno {nome} precisará fazer o reforço.')
else:
    print(f'Aluno {nome} foi aprovado.') 
print('-'*20)