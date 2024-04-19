## AWS Glue
>
> O AWS Glue é um serviço de integração de dados com tecnologia sem servidor que facilita aos usuários de análise a descoberta, preparação, transferência e integração de dados de várias fontes. Você pode usá-lo para análise, machine learning e desenvolvimento de aplicações.
>
> Já o AWS Glue Studio é uma interface gráfica que facilita a criação, a execução e o monitoramento de trabalhos de integração de dados no AWS Glue. Você pode compor visualmente fluxos de trabalho de transformação de dados e executá-los perfeitamente no mecanismo de ETL com tecnologia sem servidor baseado no Apache Spark do AWS Glue.
>
### Importações Necessárias
>
> Bibliotecas necessárias para trabalhar com o AWS Glue e o Spark.
> Isso inclui módulos para inicializar o contexto do Spark, carregar dados do S3, realizar operações de DataFrame e definir janelas de análise.
>

### Exercícios

>- Ler o arquivo nomes.csv no S3 (lembre-se de realizar upload do arquivo antes).

<img width="1840" alt="Captura de Tela 2024-03-13 às 5 28 45 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/db3c23ef-6d77-487b-b8aa-9fa31a68681f">

<img width="1840" alt="Captura de Tela 2024-03-13 às 5 28 23 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/a0036672-411b-4fb5-9cc3-f98cbc7b066f">

>- Imprima o schema do dataframe gerado no passo anterior.

 <img width="1840" alt="Captura de Tela 2024-03-13 às 5 39 38 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/f67fc24b-7fea-4dd7-891d-2cc1ab2bee94">
 
 <img width="1840" alt="Captura de Tela 2024-03-13 às 5 39 55 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/6115d297-6b51-4ef7-b4e6-9e6b6dc82958">

>- Escrever o código necessário para alterar a caixa dos valores da coluna nome para MAIÚSCULO.

 <img width="1840" alt="Captura de Tela 2024-03-13 às 6 09 01 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/f75c9e7b-e833-40f3-aa32-f29487e6e286">

 <img width="1840" alt="Captura de Tela 2024-03-13 às 6 09 21 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/30994dd9-8e14-451d-9056-4b03babbf828">

>- Imprimir a contagem de linhas presentes no dataframe. Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.
>  Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe.

 <img width="1840" alt="Captura de Tela 2024-03-13 às 6 35 39 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/d3a153d0-f9cc-40c1-97dd-833976195f88">
 
 <img width="1840" alt="Captura de Tela 2024-03-13 às 6 35 56 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/0f0bf994-5c2d-4a04-bc55-ef808d155e4e">

>- Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.
>- O script abaixo realiza a leitura do arquivo nomes.csv (S3_INPUT_PATH) e retorna o nome feminino com mais registros e o respectivo ano.

 <img width="1840" alt="Captura de Tela 2024-03-14 às 5 28 46 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/5e183981-849a-49b5-96ef-3ebc28208de0">

 <img width="1840" alt="Captura de Tela 2024-03-14 às 5 28 38 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/89ea7a78-8efb-49c0-b717-40e4dc89f2ab">

>- Apresentar qual foi o nome masculino com mais registros e em que ano ocorreu.
>- O script abaixo realiza a leitura do arquivo nomes.csv (S3_INPUT_PATH) e retorna o nome masculino com mais registros e o respectivo ano.

 <img width="1840" alt="Captura de Tela 2024-03-17 às 8 06 21 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/0cbf2c7f-f8f6-481a-865e-6bb082e517f1">

 <img width="1840" alt="Captura de Tela 2024-03-17 às 8 10 08 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/78ddc371-48f8-41d0-a026-3a771f17cc5c">

>- Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe.Considere apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente.

 <img width="1840" alt="Captura de Tela 2024-03-13 às 6 46 34 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/0b1a04f1-9038-4392-ade0-bc5c5393d33a">
 
 <img width="1840" alt="Captura de Tela 2024-03-13 às 6 46 57 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/60aab332-b999-4b06-abe0-1e4bb8efc8e5">

>- Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3.
>  Atenção aos requisitos:
>  A gravação deve ocorrer no subdiretório frequencia_registro_nomes_eua do paths3://<BUCKET>/lab-glue/ .
>  O formato deve ser JSON. O particionamento deverá ser realizado pelas colunas sexo e ano (nesta ordem).

 <img width="1840" alt="Captura de Tela 2024-03-14 às 4 05 05 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/cd710806-6bd8-4d7b-8d0c-751b075edf8c">
 
 <img width="1840" alt="Captura de Tela 2024-03-14 às 4 03 58 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/79c3c89b-5cab-4edd-bc88-0051296f2983">

## Crawler
>
> É utilizado para realizar a transição dos metadados armazenados no s3 para o aws glue, de modo que posteriormente facilite a visualização dos dados no Data Gatalog do glue.
> Crawlers são mecanismos que podemos utilizar para monitorar nosso armazenamento de dados demodo a criar/atualizar metadados no catálogo do Glue de forma automática.

<img width="1840" alt="Captura de Tela 2024-03-14 às 4 23 02 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/7df3c6c4-6524-4421-bba6-b1b17b1a923e">

>
> Pesquisa realizada no AWS Athena
>

<img width="1840" alt="Captura de Tela 2024-03-14 às 4 28 36 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/2967151e-3a7f-492d-876d-b93733589c2d">

<img width="1840" alt="Captura de Tela 2024-03-14 às 4 28 40 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/e1b5216a-bce3-4eb1-afd6-57431c4afbad">

## Permissões

> Foi concededido privilégios de DESCRIBE e SELECT no AWS LakeFormation.

<img width="1840" alt="Captura de Tela 2024-03-14 às 4 38 17 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/dbf94888-b076-4520-bb3d-625efe11feec">

