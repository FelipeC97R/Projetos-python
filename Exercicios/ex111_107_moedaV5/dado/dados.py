from moeda.moeda_operacoes import transformaReais,triplo,metade,aumentar

def linha (arg_tipoLinha):
    print(f'{arg_tipoLinha}'*40)

def resumo(arg_money, arg_increased = 0 ,arg_decreased = 0):
    linha('-')
    print('Resumo do valor')
    linha('-')
    print(f'Valor analisado: \t{transformaReais(arg_money)}')
    print(f'Dobro do valor: \t{triplo(arg_money,True)}')
    print(f'Metade do valor: \t{metade(arg_money,True)}')
    print(f'Valor com aumento de {arg_increased}%: \t{aumentar(arg_money,arg_increased,True)}')
    print(f'Valor com aumento de {arg_decreased}%: \t{aumentar(arg_money,arg_decreased,True)}')
    linha('-')