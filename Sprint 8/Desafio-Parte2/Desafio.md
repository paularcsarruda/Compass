1.  Criar nova camada (layer) no AWS Lambda para as libs necessárias à ingestão de dados.

 <img width="1840" alt="Captura de Tela 2024-03-25 às 3 30 23 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/d006bdca-ab3e-440b-8b7f-94297e93de16">

 <img width="1840" alt="Captura de Tela 2024-03-25 às 3 30 30 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/e9c1cbd7-b62b-4705-af8f-d1b2f1dce9a0">

2. Implementar o código Python em AWS Lambda para consumo de dados do TMDB:
   - Buscar, pela API, os dados que complementem a análise
   - Utilizar a lib boto3 para gravar os dados no AWS S3, em arquivos JSON, com 100 registros em cada arquivo.

  
