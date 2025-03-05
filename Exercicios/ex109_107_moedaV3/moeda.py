def triplo(arg_valor,convertToMoney = False):
    valor_triplo = arg_valor*3

    if convertToMoney is True:
        return transformaReais(valor_triplo)
    return valor_triplo


def metade(arg_valor,convertToMoney = False):
    '''
    Return a half of the provided value

    Args: 
        arg_valor (float):the monetary value received

    Returns:
        float: half of given value

    Examples:

        >>> metade(5)
        2.5
    '''
  
    valor_metade = arg_valor/2
    if convertToMoney is True:
        return transformaReais(valor_metade)
    return valor_metade

def aumentar(arg_value,arg_percentage, convertToMoney = False):
    
    increased_value = arg_value*(1+ (arg_percentage/100))
    if convertToMoney is True:
        return transformaReais(increased_value)
    return increased_value


def diminuir(arg_value,arg_percentage,convertToMoney = False):
    decreased_value = arg_value*(1 - (arg_percentage/100))
    if convertToMoney is True:
        return transformaReais(decreased_value)
    return decreased_value

def transformaReais(arg_valor,simboloDinheiro = 'R$'):
    valor_reais = f'{simboloDinheiro}{arg_valor:>.2f}'.replace('.',',')
    return valor_reais

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