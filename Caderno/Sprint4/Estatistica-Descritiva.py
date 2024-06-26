# -*- coding: utf-8 -*-
"""Aula-Estatistica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ifAI-5ML_DQjDEKGVlMjJSBBojw4kY-d

# **Gráficos de Barras e Colunas**
"""



import matplotlib.pyplot as plt
import seaborn as sns

y = [2, 5, 2, 7, 5, 1]
x = ["N1", "N2", "N3", "N4", "N5", "N6"]

plt.barh(x, y)

plt.barh(x, y, color='g')
plt.xlabel('Variável eixo x', size=20)
plt.ylabel('Categorias', size=20)
plt.title('Título do meu Gráfico', size=25)

plt.bar(x, y, color='g')
plt.xlabel('Variável eixo x', size=20)
plt.ylabel('Categorias', size=20)
plt.title('Título do meu Gráfico', size=25)

sns.barplot(x)

plt.pie(y, labels=x, radius=1)
plt.show()

y = [1, 3, 5, 7, 9]
x = [2, 4, 10, 6, 12]
x1 = ['seg', 'ter', 'qua', 'qui', 'sex']



plt.plot(y, x, 'o-r')
plt.ylabel('Eixo Y', size=20)
plt.xlabel('Eixo X', size=20)
plt.title('Título', size=25)
plt.show()

"""# **Histograma**"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)

x

plt.hist(x, color='green', bins=50) # bins são as células/intervalos
plt.xlabel('Eixo x')
plt.ylabel('Frequencia')
plt.show()

"""# **MTC - Medida de Tendência Central**

# **Cálculo da Média**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.sampledata.iris import flowers as dados

dados.shape

dados.head(3)

"""**Cálculo da Média**"""

med_sepal_length = np.mean(dados['sepal_length'])
med_sepal_length

med_sepal_width = np.mean(dados['sepal_width'])
med_sepal_width

med_petal_length = np.mean(dados['petal_length'])
med_petal_length

"""**Obter Média de TODAS as Colunas**"""

np.mean(dados)

"""# **Cálculo da Mediana**"""

mediana_sepal_length = np.median(dados['sepal_length'])
mediana_sepal_length

mediana_sepal_width = np.median(dados['sepal_width'])
mediana_sepal_width

mediana_petal_length = np.median(dados['petal_length'])
mediana_petal_length

mediana_petal_width = np.median(dados['petal_width'])
mediana_petal_width

"""# **Cálculo da Moda**"""

moda_sepal_length = dados['sepal_length'].mode()
moda_sepal_length

moda_sepal_width = dados['sepal_width'].mode()
moda_sepal_width

moda_petal_length = dados['petal_length'].mode()
moda_petal_length

moda_petal_width = dados['petal_length'].mode()
moda_petal_width

"""# **Separatrizes**"""

np.quantile

P10_sepal_length = np.quantile(dados['sepal_length'], 0.10)
P10_sepal_length

P10_sepal_width = np.quantile(dados['sepal_width'], 0.10)
P10_sepal_width

P50_sepal_length = np.quantile(dados['sepal_length'], 0.50) #igaul a mediana
P50_sepal_length

Q1_sepal_length = np.quantile(dados['sepal_length'], 0.25)
Q1_sepal_length

"""# **Informações Condensadas**
**Função Describe**
"""

dados.describe()

"""**Visão Espacial das Estatísticas Descritivas**"""

dados.head()

x = dados['sepal_length']
y = dados['sepal_width']

plt.scatter(x, y)
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')

plt.plot(np.mean(x), np.mean(y), '*r') #cálculo da media

plt.plot(np.median(x), np.median(y), 'oy') #cálculo da mediana

plt.plot(x.mode(), y.mode(), 'og') #cálculo da moda

"""# **Medidas de Dispersão**


*   Dados apresentam semelhanças e variabilidades
*   Permitem identificar até que ponto os resultados se concentram ou não ao redor da tendência central de um conjunto de observações



1.   Assimetria a Esquerda
2.   Simétrica
3.   Assimetria a Direita

**Medidas de Dispersão (MD)**



*   as medidas de dispersão auxiliam às medidas de tendÊncia central a descrever melhor os dados
*   indicam quando os dados estão ou não póximos uns dos outros

**Amplitude Total**

está relacionada a diferença entre o maior e o menor valor presente nos conjuntos de dados.

a desvantagem da amplitude total é que ela não leva em consideração os valores intermediarios e/ou como os dados estão distribuídos.

**Amplitude Interquatílica**

é dada pela diferença entre o primeiro e o terceiro quartil. É uma medida mais estável que a amplitude total, sendo útil para detectar valores discrepantes.

`dq = Q3 - Q1`

a amplitude semi-interquartílica

`dq = Q3 - Q1 / 2`

**Desvio Médio**

*   é a diferença entre cada valor observado e a média.
*   a soma dos desvios é igual a zero

**Variância e Desvio Padrão**

**Coeficiênte de Variação**

Indica a variabilidade da medida em relação a média. A vantagem de sua utilização: permite comparar dispersões de diferentes distruições de dados.
"""

dados.head(3)

dados.shape

"""**Cálculo da Amplitude Total**"""

type(dados)

dados.max()

dados.min()

dados.iloc[:, 0:4]

dados.iloc[:, 0:4].max()

dados.iloc[:, 0:4].min()

amplitude_total = dados.iloc[:, 0:4].max() - dados.iloc[:, 0:4].min()
amplitude_total

"""**Amplitude Interquartílica: dq = Q3 - Q1**"""

np.quantile(dados['sepal_length'], 0.75)

Q3 = dados['sepal_length'].quantile(0.75)

Q1 = dados['sepal_length'].quantile(0.25)

amplitude_interquartilica = Q3 - Q1
amplitude_interquartilica

dados.quantile(0.25)

dqt = dados.quantile(0.75) - dados.quantile(0.25)
dqt

"""**Desvio Médio Absoluto**"""

dados.mad() #desvio médio absoluto

"""**Variância e Desvio Padrão**"""

dados.var()

np.var(dados)

dados.std() #desvio padrão

np.std(dados)

"""**Cálculo do Coeficiênte de Variação - CV**

CV = std/media * 100
"""

cv = np.std(dados)/np.mean(dados) * 100
cv

"""# **Medidas de Assimetria**

auxiliam na construção de Histograma.

Classificação:

1. Simetricas (As = 0)
2. Assimetria Negativa (As < 0) - à esquerda
3. Assimetria Positiva (As > 0) - à direita

**Medidas de Curtose**

 essa medida quantifica a concentração ou dispersão dos valores de um conjunto de dados em relação às medidas de tendência central. É capaz de medir o grau de achatamento de uma distribuição.

 Classificação do grau de achatamento:

 1. Leptocúrtica: dado MUITO concentrado em torno do centro (K<0.263)
 2. Mesocúrtica: dados LEVEMENTE concentrados em torno do centro (K=.263)
 3. Platicúrtica: dados POUCO concentrados em torno do centro (k>0.263)

## **Boxplot com Python**
"""

import seaborn as sns
from bokeh.sampledata.iris import flowers as dados
import matplotlib.pyplot as plt

dados.head(3)

sns.boxplot(data = dados)

sns.set(style='whitegrid', color_codes=True)
sns.boxplot(data = dados)

plt.boxplot(dados['sepal_length'])
plt.show()

"""**Gráficos na Horizontal**"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

np.random.seed(seed=0)

x = np.random.randn(1000)
y = np.random.randn(100)
z = np.random.randn(10)

fig, ax = plt.subplots()
ax.boxplot((x, y, z), vert=False, showmeans=True, meanline=True,
           labels=('x', 'y', 'z'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})

plt.show()

"""#**Monte Carlo**


"""

import random

T = 8000 #tentativas de sorteios

I = 0

for i in range(T):
  x = random.random()
  y = random.random()
  if (((x*x) + (y*y)) < 1):
    I = I + 1

I

Pi = 4*I/T

Pi

"""#**Titanic Data Analysis**"""

from google.colab import files
import io

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#carrega arquivo no Colab
uploaded = files.upload()

#ler arquivo carregado para o Colab
df = pd.read_csv(io.BytesIO(uploaded['train.csv']))

#Visualizar as 3 primeiras linhas do df
df.head(3)

df.tail(3)

#saber informações gerais do nosso banco de dados
df.info()

#Estatística descritiva dos dados
df.describe()

#avaliar valores faltantes
df.isnull().sum()

#preencher valores faltantes com a média
df.fillna(df['Age']).dropna().median().inplace=True

df.isnull().sum()

#plotar sobreviventes
df.plot(kind = 'scatter', x = 'Fare', y = 'Survived', color = 'r', linewidth = 1)
plt.show()

#sobreviventes em relação a classe do navio
sns.barplot(x = 'Pclass', y = 'Survived', data = df)

