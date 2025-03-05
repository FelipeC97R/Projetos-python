def arquivoExiste(arg_nomeArquivo):
    import os
    os.chdir(r"C:\Users\FelipeCr\Documents\Projetos programação\PYTHON\Exercicios\ex115_cadastro_pessoas")
    try:
        verifica = open(arg_nomeArquivo, 'rt')
        verifica.close()
    except:
        return False
    else:
        return True
    
def criarArquivo(arg_nomeArquivo):
    import os
    os.chdir(r"C:\Users\FelipeCr\Documents\Projetos programação\PYTHON\Exercicios\ex115_cadastro_pessoas")
    try:
        criar = open(arg_nomeArquivo, 'wt+')
        criar.close()
    except:
        print('Houve algum erro')
    else:
        print(f'Arquivo {arg_nomeArquivo} criado com sucesso!')


def lerArquivo(arg_nomeArquivo):
    import os
    os.chdir(r"C:\Users\FelipeCr\Documents\Projetos programação\PYTHON\Exercicios\ex115_cadastro_pessoas")
    try:
        arquivo = open(arg_nomeArquivo, 'rt')
    except:
        print('Erro na leitura do arquivo')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<10}{dado[1]:>20}')
    finally:
        arquivo.close()

def cadastrarArquivo(arg_nomeArquivo, arg_nome = 'desconhecido',arg_idade = 0):
    import os
    os.chdir(r"C:\Users\FelipeCr\Documents\Projetos programação\PYTHON\Exercicios\ex115_cadastro_pessoas")
    
    try:
        arquivo = open(arg_nomeArquivo, 'at')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            arquivo.write(f'{arg_nome};{arg_idade}\n')
        except:
            print('Houve falha ao escreve no arquivo')