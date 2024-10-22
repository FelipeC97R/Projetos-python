'''Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numberZerotoTwenty = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze'
                      ,'Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

while True:
    userNumberChoosed = int(input('Escolha um número entre 0 e 20: '))
    
    if 0 <= userNumberChoosed <= 20:
        break

print(numberZerotoTwenty[userNumberChoosed])