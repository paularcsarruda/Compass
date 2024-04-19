def lista_numeros(filename):
    with open(filename, 'r') as file:
        numeros = map(int, file.readlines())
        numeros_pares = filter(lambda x: x % 2 == 0, numeros)
        return numeros_pares

filename = 'number.txt'

cinco_maiores = sorted(lista_numeros(filename), reverse=True)[:5]
soma_total = sum(cinco_maiores)

# Resultados
print(cinco_maiores)
print(soma_total)
