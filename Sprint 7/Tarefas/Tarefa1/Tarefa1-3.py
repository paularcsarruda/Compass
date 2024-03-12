'''
Apresente o nome do ator/atriz com a maior média por filme.
'''

import pandas as pd

# Carregando o arquivo CSV
df = pd.read_csv('/Users/paulaarruda/Desktop/Compass/Sprint 7/Tarefas/actors.csv')

df['Actor'] = df['Actor'].str.replace('"', '').str.replace(',', '')

maximo_filme = df["Number of Movies"].idxmax()

maior_media = df["Average per Movie"].idxmax()

Ator = df.loc[maior_media, "Actor"]

print(Ator)



