'''Crie um programa que leia a idade e o sexo de várias pessoas.
 A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

from time import sleep
print('-='*10,'CADASTRO DE PESSOAS','-='*10,'\n')

counterPersonLess18 = counterMan = counterWomanLessThan20 = 0
while True: 
    registredPersonAge = int(input('Digite a idade: '))
    while True:
        registredPersonSex = input('Digite o sexo [M/F]:').upper().strip()
        if registredPersonSex in ('M','F'):
            break
        print('\r','Valor digitado inválido. Tente novamente', end = '')
            
    if registredPersonSex =='M':
        counterMan += 1
    elif registredPersonAge == 'F' and registredPersonAge <= 20:
        counterWomanLessThan20 += 1

    if registredPersonAge < 18:
        counterPersonLess18 += 1       

    # Verification that the user will continue operation
    while True:
        userWantsToProceed = input ('Deseja proseguir com o cadastro [S/N]? ').upper().strip()
        if userWantsToProceed in ('S','N'):
            break
        print('Valor incorreto. Digite novamente')
    if userWantsToProceed == 'N':
        print('Cadastro finalizado')
        break
    
print(f'O total de pessoas com menos de 18 são {counterPersonLess18}\n'
      f'O total de homens são de {counterMan}\n'
      f'O total de mulheres é de menos de 20 é {counterWomanLessThan20}\n')

input('Pressione enter para sair...')