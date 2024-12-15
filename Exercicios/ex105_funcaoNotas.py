'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
 retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma                                                                                                                                                      
– A situação (opcional)'''


# classe = []
# while True:
#     aluno = {}
#     aluno['nome'] =  str(input('Nome do aluno: '))
#     nota = []
    
#     contador_notas = 1
#     while True: 
#         nota.append(int(input(f'Nota {contador_notas}: ')))
#         contador_notas += 1

#         finalizar_notas = str(input('Sair?[s/n]:')).upper().strip()
#         if finalizar_notas == 'S':
#             break
#     aluno['notas'] = nota[:]
#     classe.append(aluno.copy())
#     finalizar_alunos = str(input('Sair Alunos? ')).upper().strip()
#     if finalizar_alunos == 'S':
#         break

classe = [{'nome': 'Ana', 'notas': [5, 6]}, {'nome': 'Paulo', 'notas': [8, 3, 9]}]
total_notas = sum(len([aluno['notas']]) for aluno in classe)

for aluno in classe:
    tot_notas = len(aluno['notas'])

    
print(total_notas)