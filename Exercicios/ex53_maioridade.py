'''Crie um programa que leia o ano de nascimento de sete pessoas.
 No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import datetime


totalPeople = int(input('Digite quantas pessoas entrarão na pesquisa: '))

countMajorAge=0
for countPeople in range(1,totalPeople + 1): 

    birthDay = int(input(f'Digite data de nascimento da {countPeople}º pessoa: '))
    peopleAge = datetime.now().year - birthDay 
    if peopleAge >= 18:
        countMajorAge += 1

totalMinorAge = totalPeople - countMajorAge
print(f'O total de maiores de idade são {countMajorAge} e o total de menores são {totalMinorAge}')
