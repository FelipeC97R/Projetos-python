'''Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’
, o programa se encerrará. Importante: use cores.'''


def colorir_texto():
    cor_fundo = {'preto':0,'vermelho':1,'verde':2,'amarelo':3,'azul':4,'magenta':5,'ciano':6,'branco':7}
    cor_letra = {'preto':0,'vermelho':1,'verde':2,'amarelo':3,'azul':4,'magenta':5,'ciano':6,'branco':7}
    estilos = {'preto':0,'vermelho':1,'verde':2,'amarelo':3,'azul':4,'magenta':5,'ciano':6,'branco':7}
    
    for cor, numero in cor_fundo.items():
        print(f'{cor:<10}: {numero:>1}') 

def interactiveHelp(arg_content):
    print('~'*50)
    print(help(arg_content))
    print('~'*50)

interactiveHelp(input('Digite uma função do python que deseja tirar dúvida: '))