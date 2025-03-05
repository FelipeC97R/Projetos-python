''' Verifica se o site pudim está online'''

from urllib import request, error

try:
    request.urlopen('https://www.pudim.com.br')
except error.URLError:
    print(f'Site não conseguiu ser acessado')
else:
    print('Tudo okay')