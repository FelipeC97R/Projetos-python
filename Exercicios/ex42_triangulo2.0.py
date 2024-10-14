'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
 EQUILÁTERO: todos os lados iguais
 ISÓSCELES: dois lados iguais, um diferente
 ESCALENO: todos os lados diferentes'''

triangleSegmentA = int(input('Digite o primeiro segmento: '))
triangleSegmentB = int(input('Digite o segundo segmento: '))
triangleSegmentC = int(input('Digite o terceiro segmento: '))

if abs(triangleSegmentA - triangleSegmentB) < triangleSegmentC < triangleSegmentA + triangleSegmentB:
    if triangleSegmentA != triangleSegmentB != triangleSegmentC != triangleSegmentA:
        triangleType = 'ESCALENO'
    elif triangleSegmentA == triangleSegmentB == triangleSegmentC:
        triangleType = 'EQUILÁTERO'
    else: 
        triangleType = 'ISÓCELES'
    print(f'Os segmentos {triangleSegmentA},{triangleSegmentB},{triangleSegmentC} formam um triângulo {triangleType}')
else:
    print(f'Os segmentos {triangleSegmentA},{triangleSegmentB},{triangleSegmentC} não formam um triângulo')