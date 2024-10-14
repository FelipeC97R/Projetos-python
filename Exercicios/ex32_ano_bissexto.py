'''Determine e o ano é bissexto: 
O ano é bissexto se: 
- Precisa ser divisivel por 4
- Se for divisivel por 100 também precisa ser por 400 '''

ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0 and ano != 100 == 0 or ano % 400 == 0:
    # É divisível por 4 e não por 100?
    # Ou É divisivel 400 ?
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')