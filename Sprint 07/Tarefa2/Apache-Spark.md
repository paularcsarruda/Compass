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
> (docker pull jupyter/all-spark-notebook)
>

 <img width="1136" alt="Passo 1" src="https://github.com/paularcsarruda/Compass/assets/122739036/471b17c8-9b3f-4a67-949a-b4272b62a798">


>
> - Criar um container a partir da imagem
>
> (docker run -it -p 8888:8888 --name spark_container jupyter/all-spark-notebook)
>

 <img width="1382" alt="Captura de Tela 2024-03-17 às 10 25 08 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/5d221245-38c0-4c83-afcb-3bebb18067c8">


>
> - Acessar o Jupyter através do link: http://127.0.0.1:8888/lab?token=f01a6da42aa97feac44bc891264e338a3798f165734db1b1
>

 <img width="1837" alt="Captura de Tela 2024-03-17 às 10 11 27 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/88182276-c319-4544-b557-f3a34b556eeb">


>
> - Em outro terminal, execute o comando `pyspark` no seu container. Pesquise sobre o comando  docker exec para realizar esta ação. Utilize as flags -i e -t no comando.
>
> - Usando o Spark Shell, apresente a sequência de comandos Spark necessários para contar a quantidade de ocorrências de cada palavra contida no arquivo README.md de seu repositório git.
>

 <img width="1136" alt="Captura de Tela 2024-03-17 às 10 12 38 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/bd495511-782a-4403-8cd2-b4adaa0819c2">


### Resultado
>
> Resultado: 419 palavras
>

 <img width="1837" alt="codigo" src="https://github.com/paularcsarruda/Compass/assets/122739036/9108f5e8-3968-4dfd-87ee-a9fdac401b82">

 <img width="1837" alt="Resultado" src="https://github.com/paularcsarruda/Compass/assets/122739036/211132cc-cfc4-4838-8fb5-53cf01877e37">


