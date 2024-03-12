'''
Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
'''

import pandas as pd

# Carregando o arquivo CSV
df = pd.read_csv('/Users/paulaarruda/Desktop/Compass/Sprint 7/Tarefas/actors.csv')

df['Actor'] = df['Actor'].str.replace('"', '').str.replace(',', '')

ator_mais_filmes = df[df['Number of Movies'] == df['Number of Movies'].max()]

# Imprimindo o resultado
print(f"O ator/atriz com o maior número de filmes é {ator_mais_filmes['Actor'].values[0]} com {ator_mais_filmes['Number of Movies'].values[0]} filmes.")
