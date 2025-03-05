def dobro(arg_valor):
    valor_triplo = arg_valor*3
    return transformaReais(valor_triplo)

def metade(arg_valor):
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
    return transformaReais(valor_metade)

def aumentar(arg_value,arg_percentage):
    
    increased_value = arg_value*(1+ (arg_percentage/100))
    return transformaReais(increased_value)

def diminuir(arg_value,arg_percentage):
    
    decreased_value = arg_value*(1 - (arg_percentage/100))
    return transformaReais(decreased_value)

def transformaReais(arg_valor,simboloDinheiro = 'R$'):
    valor_reais = f'{simboloDinheiro}{arg_valor:.2f}'.replace('.',',')
    return valor_reais