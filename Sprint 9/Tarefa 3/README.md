# Desafio - Parte I

## Processamento da Trusted

OBS.:Maicon, na segunda e terceira parte do desafio, incluí as informações de uma API da OMDB. Este trabalho será desenvolvido nas próximas semanas durante a Sprint 10. Descobri essa API no sábado à tarde e, como precisarei fazer algumas modificações, não teria tempo suficiente para concluir tudo novamente.


>
> O objetivo da tarefa 3 era criar a camada *Trusted*, a partir do arquivo gerado na sprint anterior. O arquivo resultante dessas duas etapas foi salvo na camada *Trusted* do AWS S3.
>

<img width="1837" alt="Captura de Tela 2024-04-13 às 6 49 43 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/52329ac6-63ca-42d2-b897-db4fdec284fb">

<img width="1837" alt="Captura de Tela 2024-04-13 às 6 49 47 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/da954374-2039-47b1-b933-133e66bfc8b0">


>
> Foi desenvolvido o código para converter os arquivos JSON da pasta RAW (CSV e TMDB) para PARQUET, sendo os arquivos carreagdos para a pasta *Trusted*.
>
> Os dois Job's do AWS Glue, foram desenvolvidos utilizando o *Spark Script Editor* com as configurações solicitadas na atividade.
>

<img width="1837" alt="Captura de Tela 2024-04-13 às 6 49 25 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/56d1dd7d-7a88-4f17-a430-ea2b7984a391">

<img width="1837" alt="Captura de Tela 2024-04-13 às 6 49 30 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/1c4d7b21-9a7a-491f-87b9-86391a1d024b">

<img width="1837" alt="Captura de Tela 2024-04-13 às 6 49 07 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/f135e519-b7ad-4e90-8952-54e0109a0bee">

<img width="1837" alt="Captura de Tela 2024-04-13 às 6 49 11 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/78b10fb1-0d6c-441d-a9ab-403d78d5eba0">

>
> Consultas SQL realizadas no AWS S3, nos buckets *trustedcvs* e *trustedtmdb*
>

<img width="1837" alt="Captura de Tela 2024-04-14 às 10 19 53 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/821f3767-2355-4db1-99c1-f4dc154a3ad7">
 
<img width="1837" alt="Captura de Tela 2024-04-14 às 10 20 10 AM" src="https://github.com/paularcsarruda/Compass/assets/122739036/146ba5d8-0ec5-4a5b-9dfe-6aaf247d68dc">
