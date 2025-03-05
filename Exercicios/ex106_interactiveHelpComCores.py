'''Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’
, o programa se encerrará. Importante: use cores.'''


def colorir_texto(arg_texto, argEscolhaEstilo, argEscolhaCorTexto, argEscolhaFundo):
    cor_fundo = {'preto': 0, 'vermelho': 1, 'verde': 2, 'amarelo': 3, 'azul': 4, 'magenta': 5, 'ciano': 6, 'branco': 7}
    cor_texto = {'preto': 0, 'vermelho': 1, 'verde': 2, 'amarelo': 3, 'azul': 4, 'magenta': 5, 'ciano': 6, 'branco': 7}
    estilos = {'nenhum': 0, 'negrito': 1, 'sublinhado': 4, 'negativo': 7}

    # Código de escape ANSI para colorir o texto
    codigo_escape = f'\033[{estilos[argEscolhaEstilo]};3{cor_texto[argEscolhaCorTexto]};4{cor_fundo[argEscolhaFundo]}m'
    reset_escape = '\033[0m'  # Reseta a cor ao final

    # Retorna o texto colorido
    return f'{codigo_escape}{arg_texto}{reset_escape}'


def interactiveHelp(arg_content):
    # Captura a saída da função help em uma string
    from io import StringIO
    import sys

    buffer = StringIO()
    sys.stdout = buffer
    help(arg_content)  # Redireciona a saída do help para o buffer
    sys.stdout = sys.__stdout__  # Restaura a saída padrão

    conteudo = buffer.getvalue()  # Obtém o conteúdo do buffer

    # Exibe o conteúdo colorido
    print('~' * 50)
    print(colorir_texto(conteudo, 'sublinhado', 'preto', 'amarelo'))
    print('~' * 50)


# Exemplo de uso
interactiveHelp(print)



