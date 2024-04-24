# Desafio - Parte 1
![Static Badge](https://img.shields.io/badge/Tema-Filmes_e_S%C3%A9ries-e0913e)
![Static Badge](https://img.shields.io/badge/Categoria-Drama/Romance-ffd966)

>
> Objetivo: criar código Python que carrega arquivos CSV para a Nuvem utilizando as técnicas de ETL.
>
> Ingestão Batch: a ingestão dos arquivos CSV em Bucket Amazon S3 RAW Zone. Nesta etapa do desafio deve ser construído um código Python que será executado dentro de um container Docker para carregar os dados locais dos arquivos para a nuvem. Nesse caso utilizaremos, principalmente, as lib boto3 como parte do processo de ingestão via batch para geração de arquivo (CSV).
>
>Ler os 2 arquivos (filmes e series) no formato CSV inteiros, ou seja, sem filtrar os dados.
>

## Código Python
>
> 1. Implementar código Python:
> Utilizar a lib boto3 para carregar os dados para a AWS
> acessar a AWS e gravar no S3, no bucket definido com RAW Zone
>

 <img width="1837" alt="Codigo-Python" src="https://github.com/paularcsarruda/Compass/assets/122739036/3f081696-4193-4fa1-a080-2d840f7c6138">

## Dockerfile
>
> 2. Criar container Docker com um volume para armazenar os arquivos CSV e executar processo Python implementado.
>

 <img width="1572" alt="Dockerfile" src="https://github.com/paularcsarruda/Compass/assets/122739036/18550fdf-ea48-4fb7-b78e-137fd1bb8910">
 
 <img width="1837" alt="Captura de Tela 2024-03-16 às 1 24 41 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/881adc5e-6403-4760-bb8e-cfcede1c626a">

## Carga dos dados no Bucket S3

 <img width="1840" alt="Captura de Tela 2024-03-16 às 1 32 41 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/9075e1eb-7428-42f1-bed8-b7d05ac819cf">

 <img width="1840" alt="Captura de Tela 2024-03-16 às 1 32 34 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/aafb84c5-3449-462c-822d-d4c08165c030">

 <img width="1840" alt="Captura de Tela 2024-03-16 às 1 32 31 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/7955ad92-773b-4521-9cb4-cfd1ef6e18af">

 <img width="1840" alt="Captura de Tela 2024-03-16 às 1 32 26 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/0c9fa0b9-bd92-4d4b-9c89-afecad7f1027">
