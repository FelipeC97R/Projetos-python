
totalPeople = int(input('Quantas pessoas serão comparadas: '))
for i in range (0,totalPeople):
    weightPeople = float(input(f'Digite o valor do peso da {i}º pessoa:'))
    if i == 0:
        minWeight = weightPeople
        maxWeight = minWeight
    if weightPeople > maxWeight:
        maxWeight = weightPeople
    if  weightPeople < minWeight:
        minWeight = weightPeople

print(f'O maior peso: {maxWeight:.2f} ')
print(f'O menor peso: {minWeight:.2f} ')
