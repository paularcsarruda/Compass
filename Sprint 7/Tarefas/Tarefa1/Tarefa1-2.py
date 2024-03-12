'''
Apresente a média da coluna contendo o número de filmes.
'''

import pandas as pd
# Carregando o arquivo CSV
df = pd.read_csv('/Users/paulaarruda/Desktop/Compass/Sprint 7/Tarefas/actors.csv')

# Removendo aspas e vírgulas do nome do ator/atriz
df['Actor'] = df['Actor'].str.replace('"', '').str.replace(',', '')

# Convertendo a coluna 'Number of Movies' para numérica
df['Number of Movies'] = pd.to_numeric(df['Number of Movies'], errors='coerce')

# Calculando a média da coluna desejada
media = df['Number of Movies'].mean()

# Imprimindo o resultado
print(f"A média da coluna número de filmes é {media}.")