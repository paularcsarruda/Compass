'''
Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
'''

import pandas as pd

# Carregando o arquivo CSV
df = pd.read_csv('/Users/paulaarruda/Compass/Sprint 7/Tarefas/Tarefa1/actors.csv')

dfCount = df["#1 Movie"].value_counts().reset_index()
dfCount.columns = ["Filmes", "Frequência"]
dfCount = dfCount[dfCount["Frequência"] > 1]
print(dfCount)
