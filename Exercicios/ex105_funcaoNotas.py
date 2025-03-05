'''Faça um programa pode receber várias notas de alunos e vai
 retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média das notas                                                                                                                                                      
– A situação (opcional)'''

def notas(*argNotas,situacao=False):
    maiorNota = max(argNotas)
    menorNota = min(argNotas)
    media = sum(argNotas)/len(argNotas)

    print(f'Maior nota: {maiorNota}')
    print(f'Menor nota: {menorNota}')
    print(f'Média : {media}')
    if situacao ==True:
        print('Aprovado' if media>=7 else 'Reprovado')

notas(1,2,3,4,situacao=True)