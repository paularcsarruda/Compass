from pyspark import SparkContext, SparkConf 
import re

sc = SparkContext.getOrCreate()
# Arquivo README.md
rdd = sc. textFile("/home/jovyan/README.md")

# Removendo as tags HTML
rdd_words = rdd.flatMap(lambda linha: re.findall(r'\b|w+\b', linha))

# Filtrando as palavras vazias
rdd_words = rdd_words.filter(lambda palavra: len(palavra) > 0)

# Contando as ocorrências de cada palavra
contagem = rdd_words.map(lambda palavra: (palavra. lower(), 1)) \
                    .reduceByKey(lambda a, b: a + b) \
                    .sortByKey()

total_palavras = rdd_words.count()
resultado = contagem.collect ()

for word, count in resultado:
    print(f'{word}: {count}')


print(f'Total de palavras: {total_palavras}')
sc.stop()