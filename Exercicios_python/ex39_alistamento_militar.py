'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do 
tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import datetime

candidateBirthYear = int(input('Digite aqui o ano em que você nasceu: '))
year_today = datetime.now().year
candidateAge = year_today - candidateBirthYear 
enlistment_age = 18
yearCandidateCanEnlist = candidateBirthYear + enlistment_age

if candidateAge <= 0:
    print('Idade inválida')
else:
    print(f'Estamos no ano de {year_today} e atualmente você tem {candidateAge} anos')
    print(f'\nA sua data de alistamento é no ano {yearCandidateCanEnlist}')
    if candidateAge > enlistment_age: 
        print('Passou do prazo de se alistar')
        print(f'Está atrasado {year_today - yearCandidateCanEnlist} em anos para o alistamento')
    elif candidateAge == enlistment_age:
        print('Está na hora de se alistar')
    else:
        print('Você é muito novo para se alistar')
        print(f'Faltam {yearCandidateCanEnlist - year_today} anos para você se alistar')
 
    
