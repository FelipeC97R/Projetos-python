'''Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’
, o programa se encerrará. Importante: use cores.'''



    
def interactiveHelp(arg_content):
    print('~'*50)
    print(help(arg_content))
    print('~'*50)

interactiveHelp(input('Digite uma função do python que deseja tirar dúvida: '))