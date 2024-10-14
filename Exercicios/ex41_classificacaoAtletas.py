'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: SÊNIOR
Acima de 25 anos: MASTER'''

#INPUTS PARA TESTE DO PROGRAMA
# athleteName = 'Felipe'
# swimExperienceYears = 10

athleteName = input('Nome do atleta:')
swimExperienceYears = int(input('Idade do atleta: '))

if swimExperienceYears <=0:
    print('Idade inválida!')
else:
    if  swimExperienceYears <=9:
        swimmingCategorie = 'MIRIM'
    elif swimExperienceYears <=14:
        swimmingCategorie = 'INFANTIL'
    elif swimExperienceYears <=19:
        swimmingCategorie = 'JÚNIOR'
    elif swimExperienceYears <=25:
        swimmingCategorie = 'SÊNIOR'
    else:
        swimmingCategorie = 'MASTER'
    
    print(f'Categoria do atleta : {swimmingCategorie}')