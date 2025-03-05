def colorir_texto(arg_texto, argEscolhaEstilo ='nenhum', argEscolhaCorTexto = 'branco', argEscolhaFundo = 'preto'):
    cor_fundo = {'preto': 0, 'vermelho': 1, 'verde': 2, 'amarelo': 3, 'azul': 4, 'magenta': 5, 'ciano': 6, 'branco': 7}
    cor_texto = {'preto': 0, 'vermelho': 1, 'verde': 2, 'amarelo': 3, 'azul': 4, 'magenta': 5, 'ciano': 6, 'branco': 7}
    estilos = {'nenhum': 0, 'negrito': 1, 'sublinhado': 4, 'negativo': 7}
    
    texto_colorido = f'\033[{estilos[argEscolhaEstilo]};3{cor_texto[argEscolhaCorTexto]};4{cor_fundo[argEscolhaFundo]}m{arg_texto}\033[m'
    return texto_colorido


def linha_cabecalho (arg_mensagem):
    print('-'*(34))
    print(f'{arg_mensagem:^{34}}')
    print('-'*(34))



def linha_unica(arg_tipo = '-',arg_tamanho  = 20):
    print(arg_tipo * arg_tamanho)

def menu ():
    linha_cabecalho('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    linha_unica(arg_tamanho = 34)

def testa_inteiro(arg_texto):
    while True:
        try:
            opcao = int(input(arg_texto))
            return opcao
        except:
            print('O valor não é um número inteiro, tente novamente')

