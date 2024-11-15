'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
for i in range (1):
    aluno['nome']= str(input('Digite o nome do aluno: '))
    aluno['media'] = float(input(f'Digite a média de notas de {aluno["nome"]}: '))

    print(f'O aluno {aluno["nome"]}, tem a média {aluno["media"]}')
    if aluno['media'] < 7:
        aluno ['situacao'] = 'Reprovado'
    else:
        aluno ['situacao'] = 'Aprovado'

print(aluno)

