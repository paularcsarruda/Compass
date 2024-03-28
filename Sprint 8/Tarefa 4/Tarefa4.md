# Tarefa 4

1. Nesta etapa, adicione código para ler o arquivo nomes_aleatorios.txt através do comando spark.read.csv.
   Carregue-o para dentro de um dataframe chamado df_nomes e, por fim, liste algumas linhas através do método show.

   Exemplo: df_nomes.show(5)

   <img width="1703" alt="E1" src="https://github.com/paularcsarruda/Compass/assets/122739036/d5f16d54-54a0-43e3-9934-1a2ceb154175">

2. Nesta etapa, será necessário adicionar código para renomear a coluna para Nomes, imprimir o esquema e mostrar 10 linhas do dataframe.

   <img width="1703" alt="E2" src="https://github.com/paularcsarruda/Compass/assets/122739036/93a42c69-03c5-4701-a6bf-d86dc17f2071">

3. Ao dataframe (df_nomes), adicione nova coluna chamada Escolaridade e atribua para cada linha um dos três valores de forma aleatória: Fundamental, Medio ou Superior.

   <img width="1703" alt="E3" src="https://github.com/paularcsarruda/Compass/assets/122739036/6aff9fdc-55b6-4cc0-85da-e5e623a3b7b3">

4. Ao dataframe (df_nomes), adicione nova coluna chamada Pais e atribua para cada linha o nome de um dos 13 países da América do Sul, de forma aleatória.

   <img width="1703" alt="E4" src="https://github.com/paularcsarruda/Compass/assets/122739036/c1225150-17b4-4912-8663-6bd661c9d38d">

5. Ao dataframe (df_nomes), adicione nova coluna chamada AnoNascimento e atribua para cada linha um valor de ano entre 1945 e 2010, de forma aleatória.

   <img width="1703" alt="E5" src="https://github.com/paularcsarruda/Compass/assets/122739036/fe349148-4bfe-4873-b34f-5143c4b72f38">

6. Usando o método select do dataframe (df_nomes), selecione as pessoas que nasceram neste século. Armazene o resultado em outro dataframe chamado df_select e mostre 10 nomes deste.
   
   <img width="1703" alt="E6" src="https://github.com/paularcsarruda/Compass/assets/122739036/b6bd283c-f42c-48ee-9f0d-9f9c229997a1">

7. Usando Spark SQL repita o processo da Pergunta 6. Lembre-se que, para trabalharmos com SparkSQL, precisamos registrar uma tabela temporária e depois executar o comando SQL.
   
  <img width="1703" alt="E7" src="https://github.com/paularcsarruda/Compass/assets/122739036/06694157-3e0f-4500-8932-7d2b30af75c7">

8. Usando o método select do Dataframe df_nomes, Conte o número de pessoas que são da geração Millennials (nascidos entre 1980 e 1994) no Dataset

   <img width="1703" alt="E8" src="https://github.com/paularcsarruda/Compass/assets/122739036/bb725ba4-1942-4cf0-89a8-3dc47561c3c6">

9. Repita o processo da Pergunta 8 utilizando Spark SQL

   <img width="1703" alt="E9" src="https://github.com/paularcsarruda/Compass/assets/122739036/90ffe341-d688-4ba3-ae22-889d2b905f26">

10. Usando Spark SQL, obtenha a quantidade de pessoas de cada país para uma das gerações abaixo. Armazene o resultado em um novo dataframe e depois mostre todas as linhas em ordem crescente de Pais, Geração e Quantidade
      - Baby Boomers – nascidos entre 1944 e 1964;
      - Geração X – nascidos entre 1965 e 1979;4
      - Millennials (Geração Y) – nascidos entre 1980 e 1994;
      - Geração Z – nascidos entre 1995 e 2015.

   <img width="1837" alt="Captura de Tela 2024-03-28 às 4 00 46 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/ec8824f1-4590-45a0-b2b7-8642aaad9dec">

   <img width="1837" alt="Captura de Tela 2024-03-28 às 4 00 42 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/aa614108-db64-46f3-9677-4c35046aafdc">


