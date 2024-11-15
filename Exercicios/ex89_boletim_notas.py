'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
 No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
   notas de cada aluno individualmente.'''

boletim = []
aluno = []
while True:
    notas = []
    aluno.append(input('Nome completo aluno: '))
    
    for n in range(2):
        notas.append(input(f'Digite a {n}º nota: '))
    
    aluno.append(notas[:])
    boletim.append(aluno[:])

    aluno.clear()
    adicionar_aluno = input('Gostaria de adicionar mais alunos?[S/N]').upper().strip()
    if adicionar_aluno == 'N':
        break

print(boletim)

aluno_procurado = input('Escolha 1 aluno: ').upper()
for nome, nota in boletim:
    if aluno_procurado in nome:
        print(nota)