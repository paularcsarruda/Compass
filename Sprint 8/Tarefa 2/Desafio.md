# Parte 2 - Desafio

O objetivo desta etapa é complementar os dados dos Filmes e Series, carregados na Etapa 1, com dados oriundos do TMDB. 
Opcionalmente, você pode complementar com mais dados de outra API de sua escolha.

1.  Criar nova camada (layer) no AWS Lambda para as libs necessárias à ingestão de dados.

 <img width="1840" alt="Captura de Tela 2024-03-25 às 3 30 23 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/12e210f7-26e3-4614-b817-44324ec6e7cb">
 
 <img width="1840" alt="Captura de Tela 2024-03-25 às 3 30 30 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/db056680-5bc2-49d5-bf5a-5143cfb4dfa8">

2. Implementar o código Python em AWS Lambda para consumo de dados do TMDB:
>
> - Buscar, pela API, os dados que complementem a análise
> - Utilizar a lib boto3 para gravar os dados no AWS S3, em arquivos JSON, com 100 registros em cada arquivo.
>

 <img width="1840" alt="Captura de Tela 2024-03-27 às 11 39 47 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/fe5986ac-b95a-4126-a515-159090b36779">
 
 <img width="1840" alt="Captura de Tela 2024-03-27 às 11 38 54 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/4cc5c04b-9888-443a-865d-c512c8543da0">

 <img width="1840" alt="Captura de Tela 2024-03-27 às 11 39 37 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/6a89f747-9f97-4b3f-a94f-aa72f2ac304b">

3. Podemos utilizar os serviços CloudWatch Event ou Amazon EventBridge para agendar extrações periódicas de dados no Twitter de forma automática.

>
> - Foi utilizado o Amazon EventBridge - Scheduler para automatizar o Lamnda, sempre as 10h do dia 1.º de cada mês.
>   
 
 <img width="1837" alt="gatilho 1" src="https://github.com/paularcsarruda/Compass/assets/122739036/e6f00713-deaa-4531-8bdd-23392b5e65b5">

 <img width="1837" alt="Gatilho2" src="https://github.com/paularcsarruda/Compass/assets/122739036/7ee9bd16-11fd-40e0-abc3-16104a229d36">

4. Variáveis de Ambiente
   
>
> - criação das variáveis de ambiente para proteger as chaves da API e da AWS
>

  <img width="1840" alt="Captura de Tela 2024-03-27 às 11 47 08 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/e95669f1-8afa-4e4e-a036-c0350cfe731d">

