'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
aluno1 =str(input('Aluno 1: '))
aluno2 = input('Aluno 2: ')
aluno3 = input('Aluno 3: ')
aluno4 = input('Aluno 4: ')

lista_quadro = [aluno1,aluno2,aluno3,aluno4]
print(f'O nome escolhido é {random.choice(lista_quadro)}')