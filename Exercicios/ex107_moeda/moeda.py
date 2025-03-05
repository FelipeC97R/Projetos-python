'''Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’
, o programa se encerrará. Importante: use cores. (ex 106)
'''


def colors (arg_style, arg_TextColor,arg_backgroundColor):
    
    backgroundColor_Data = {'black': 0, 'red': 1, 'green': 2, 'yellow': 3, 'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7}  
    textColor_Data = {'black': 0, 'red': 1, 'green': 2, 'yellow': 3, 'blue': 4, 'magenta': 5, 'cyan': 6, 'white': 7}  
    styles = {'none': 0, 'bold': 1, 'underlined': 4, 'negative': 7}  
