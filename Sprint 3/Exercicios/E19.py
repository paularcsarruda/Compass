import random

random_list = random.sample(range(500), 50)
sorted_list = sorted(random_list) # lista em ordem crescente

mediana = 0
media = 0
valor_minimo = 0
valor_maximo = 0

mediana = sorted_list[len(sorted_list) // 2] if len(sorted_list) % 2 != 0 else (sorted_list[len(sorted_list) // 2 - 1] 
          + sorted_list[len(sorted_list) // 2]) / 2

media = sum(random_list) / len(random_list)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')