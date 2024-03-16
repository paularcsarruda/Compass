# Apache Spark
>
> O Apache Spark é um framework de código fonte aberto para computação distribuída. O Spark é um mecanismo de análise unificado para processamento de dados em grande escala com módulos integrados para SQL, streaming, machine learning e processamento de gráficos.
>
> O Spark pode ser executado no Apache Hadoop, Apache Mesos, Kubernetes, por conta própria, na nuvem e em diversas fontes de dados.
>
## Passo-a-Passo
>
> - Realizar o pull da imagem jupyter/all-spark-notebook
>

 <img width="1728" alt="Passo 1" src="https://github.com/paularcsarruda/Compass/assets/122739036/2695bda8-bfd6-4707-adf1-f2fd3b20a158">

>
> - Criar um container a partir da imagem
>

 <img width="1840" alt="Passo 2" src="https://github.com/paularcsarruda/Compass/assets/122739036/19c7bb83-ab61-4fe9-9585-81d20b55342c">

>
> - Acessar o Jupyter
>

 <img width="1837" alt="Jupyter" src="https://github.com/paularcsarruda/Compass/assets/122739036/99a35f92-076a-4d05-9de5-8f5b024d2010">

>
> - Em outro terminal, execute o comando `pyspark` no seu container. Pesquise sobre o comando  docker exec para realizar esta ação. Utilize as flags -i e -t no comando.
>

 <img width="1728" alt="Passo 3" src="https://github.com/paularcsarruda/Compass/assets/122739036/b8d7188e-b4b7-4214-9022-2d22f6f883e7">

>
> - Usando o Spark Shell, apresente a sequência de comandos Spark necessários para contar a quantidade de ocorrências de cada palavra contida no arquivo README.md de seu repositório git.
>

<img width="1728" alt="Python - contador" src="https://github.com/paularcsarruda/Compass/assets/122739036/97a0a977-c42d-478a-8582-2ec69169f255">

### Resultado
>
> Resultado: 580
>

 <img width="1728" alt="Resultado" src="https://github.com/paularcsarruda/Compass/assets/122739036/bd78a02c-66ed-4d9a-a479-8358a1543e48">

