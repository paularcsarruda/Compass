def soma_numeros():
    numeros = '1, 3, 4, 6, 10, 76'
    numeros_split = numeros.split(',')
    soma = 0
    
    for i in numeros_split:
        numeros_int = int(i)
        soma += numeros_int
    return soma

resultado = soma_numeros()
print(resultado)
