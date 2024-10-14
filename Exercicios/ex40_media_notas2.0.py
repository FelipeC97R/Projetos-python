''' Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO'''

# INPUTS PARA TESTE DO PROGRAMA
# studentName = 'Felipe'
# examSubject = 'Biologia'
# avarageGrade = float(6.9)

studentName = input('Nome do aluno: ')
examSubject = input('Matéria: ')
studentGrade1 = float(input(f'Primeira nota do {studentName}: '))
studentGrade2 = float(input(f'Segunda nota do {studentName}: '))
avarageGrade = (studentGrade1+studentGrade2)/2
if avarageGrade < 5:
    resultStatus = 'Reprovado'
elif  5 <= avarageGrade < 7:
    resultStatus = 'Recuperação'
else: 
    resultStatus = 'Aprovado'

print(f'Resultado do aluno {studentName} na prova de {examSubject}: {avarageGrade:.1f}\n'
      f'Status: {resultStatus}')