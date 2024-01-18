def sliced(lista):
    total = len(lista) // 3
    parte1 = lista[:total]
    parte2 = lista[total:2*total]
    parte3 = lista[2*total:]
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = sliced(lista)

print((parte1), (parte2), (parte3))