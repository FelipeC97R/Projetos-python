'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. '''

first_term = term = 3
razao =  3
n = 5
print(first_term,end=' ')
for i in range (n-1):
    term += 3
    print(term,end=' ')