# Tarefa1

## Modelagem Relacional - Normatização

>
> Para normalizar a tabela *tb_locacao*, podemos identificar as dependências funcionais presentes e dividir
a tabela em várias tabelas menores, evitando a redundância de dados e melhorando a estrutura do banco de
dados.
>
> - **1ª Forma Normal (1NF):**
Vamos garantir que cada coluna contenha apenas valores atômicos e não repetidos. Nenhuma mudança é 
necessária para atingir a 1ª Forma Normal, pois a tabela já possui valores atômicos em suas colunas.
>
> - **2ª Forma Normal (2NF):**
Para atingir a 2ª Forma Normal, devemos garantir que todas as colunas não-chave sejam totalmente 
dependentes da chave primária. Podemos dividir a tabela em três novas tabelas: *tb_locacao*, *tb_cliente*
e *tb_carro*.
>

<img width="1840" alt="Captura de Tela 2024-04-04 às 1 48 27 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/e09ff0e6-6cc5-42e9-91e4-d73a52ddc134">

<img width="1840" alt="Captura de Tela 2024-04-04 às 2 46 01 PM" src="https://github.com/paularcsarruda/Compass/assets/122739036/e61692f4-76c9-4652-9c0c-f8d9611571d5">
