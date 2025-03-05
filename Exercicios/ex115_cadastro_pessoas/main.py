'''Criar um menu de cadastro para nome e idade de pessoas'''

from biblioteca.arquivos.mod_arquivo import *
from biblioteca.interface.texto import *
from time import sleep

colorir_texto('teste',argEscolhaCorTexto='vermelho')

nomeArquivo = 'alunos.txt'
if arquivoExiste(nomeArquivo):
    print('Arquivo já existe')
else:
    criarArquivo(nomeArquivo)

while True:
    menu()
    opcao = testa_inteiro('Opção: ')
    sleep(1)
    if opcao == 1:
        linha_cabecalho('Pessoas cadastradas')
        lerArquivo(nomeArquivo)
    
    elif opcao == 2:
        linha_cabecalho(f'Cadastro novo')
        nome = str(input('Nome: '))
        idade = testa_inteiro('Idade: ')
        cadastrarArquivo(nomeArquivo,nome,idade)

    elif opcao == 3:
        linha_cabecalho(f'Saindo do sistema')
        break
    else:
        print('Opção inválida, Tente novamente')

    sleep(1)
