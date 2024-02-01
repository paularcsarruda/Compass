def calcular_valor_maximo(operadores, operandos) -> float:
    zipped = zip(operadores, operandos)
    valores_calculados = map(lambda op_xy: eval(f'{op_xy[1][0]}{op_xy[0]}{op_xy[1][1]}'), zipped)
    return max(valores_calculados)

# Teste
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

maior_valor = calcular_valor_maximo(operadores, operandos)
print(maior_valor)