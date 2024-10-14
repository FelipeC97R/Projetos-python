from math  import pow

userWeight = float(input('Digite o valor do seu peso [Kg]: '))
userHeight = float(input('Digite o valor da sua altura [m]: '))
IMC = userWeight / pow(userHeight,2)
if IMC < 18.5:
    resultCategoryIMC = 'Abaixo do peso'
elif 18.5 <= IMC < 25: 
    resultCategoryIMC = 'Peso ideal'
elif 25 <= IMC < 30: 
    resultCategoryIMC = 'Sobrepeso'
elif 30 <= IMC <= 40: 
    resultCategoryIMC = 'Obeso'
elif 40 < IMC : 
    resultCategoryIMC = 'Obesidade Mórbida'
print(f'Classificação do IMC: {IMC:.2f}, {resultCategoryIMC}')
minHealthyIMC = 18.5
maxHealthyIMC = 25
idealWeightMax = maxHealthyIMC * pow(userHeight,2)
idealWeightMin = minHealthyIMC * pow(userHeight,2)
print(f'O seu peso ideal deve estar entre {idealWeightMin} e {idealWeightMax}')