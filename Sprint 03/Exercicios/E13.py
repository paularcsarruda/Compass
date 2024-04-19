def my_map(list, f):
    resultado = []

    for item in list:
        resultado.append(f(item))
    return resultado


def potencia(x):
    return x ** 2

f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(f,potencia)
print(resultado)
    