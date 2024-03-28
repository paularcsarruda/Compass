# Desafio - Parte 2

1.  Criar nova camada (layer) no AWS Lambda para as libs necessárias à ingestão de dados.
>
> - criação da função *myFunctionDesafio*
> - criação da nova Layer
>   

 <img width="1840" alt="Captura de Tela 2024-03-25 às 3 30 23 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/0c85c61b-b2fb-4753-81ed-c6b3e3fc169b">

 <img width="1840" alt="Captura de Tela 2024-03-25 às 3 30 30 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/c535dced-2ad5-443e-ba13-e68ad2b40b53">

2. Implementar o código Python em AWS Lambda para consumo de dados do TMDB:
>   
> - Buscar, pela API, os dados que complementem a análise
> - Utilizar a lib boto3 para gravar os dados no AWS S3, em arquivos JSON, com 100 registros em cada arquivo.
> - Criação das variáveis de ambiente para proteger as chaves da API e da AWS
>

 <img width="1837" alt="Captura de Tela 2024-03-25 às 9 47 06 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/f0992908-fb8b-480e-a1ab-6109814b2235">

 <img width="1840" alt="Captura de Tela 2024-03-27 às 11 39 47 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/6f058062-56d2-43b5-84d9-fa026ad41b4f">

 <img width="1840" alt="ingestao de dados" src="https://github.com/paularcsarruda/Compass/assets/122739036/b29c0467-bd12-429d-9b0a-2665bf2a346a">

 <img width="1840" alt="s3" src="https://github.com/paularcsarruda/Compass/assets/122739036/47e29168-a676-459f-b772-d1db145c25b9">
 
 <img width="1840" alt="Captura de Tela 2024-03-28 às 1 32 27 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/65aa4ff7-3a06-485a-af10-bffe34ccd953">

 <img width="1840" alt="chaves" src="https://github.com/paularcsarruda/Compass/assets/122739036/41c848c6-19cc-4f15-bb85-4a9626583749">

3. Utilização do Amazon EventBridge para agendar extrações periódicas de dados no TMBD via Lambda de forma automática.
>
> - O cronograma *auto_lambda_desafio* foi criado utilizando o EventBridge - scheduler, com agendamentos períodicos sempre no 1.º dia de cada mês às 10h e durante todo o ano de 2024.
>   
 
 <img width="1837" alt="gatilho 1" src="https://github.com/paularcsarruda/Compass/assets/122739036/135a4799-1f7d-4dbf-bcda-3e27e440cb48">
 

 <img width="1837" alt="Gatilho2" src="https://github.com/paularcsarruda/Compass/assets/122739036/22a03c98-312e-40e8-aed3-4f8d6bbfc685">
