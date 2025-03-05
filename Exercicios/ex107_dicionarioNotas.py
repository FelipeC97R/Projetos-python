'''Faça um programa pode receber várias notas de alunos e vai
 retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma                                                                                                                                                      
– A situação (opcional)'''


classe = []
while True:
    aluno = {}
    aluno['nome'] =  str(input('Nome do aluno: '))
    nota = []
    
    contador_notas = 1
    while True: 
        nota.append(int(input(f'Nota {contador_notas}: ')))
        contador_notas += 1

        finalizar_notas = str(input('Sair?[s/n]:')).upper().strip()
        if finalizar_notas == 'S':
            break
    aluno['notas'] = nota[:]
    classe.append(aluno.copy())
    finalizar_alunos = str(input('Sair Alunos? ')).upper().strip()
    if finalizar_alunos == 'S':
        break


total_notas = sum(len(aluno['notas']) for aluno in classe)

maior_nota = max(max(aluno['notas'])for aluno in classe)
menor_nota = min(min(aluno['notas'])for aluno in classe)
print(maior_nota)
print(menor_nota)

media_turma = sum(sum(aluno['notas'])for aluno in classe)/total_notas
print(total_notas)
print(media_turma)

nome_aluno = input('Digite o nome do aluno: ').upper()
for aluno in classe:
    if aluno['nome'].upper() == nome_aluno:
        for k, v in aluno.items():
            print(f'{k}:{v}')