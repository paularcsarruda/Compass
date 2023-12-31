
# COMANDO SELECT

-- (exemplo 1) Seleção de uma coluna de uma tabela
- Liste os e-mails dos clientes da tabela sales.customers

select email
from sales.customers

-- (exemplo 2) Seleção de mais de uma tabela 
- Liste os e-mails e nomes dos clientes da tabela sales.customers

select email, first_name, last_name
from sales.customers

-- (exemplo 3) Seleção de todas as tabelas
- Liste todas as informações dos clientes da tabela sales.customers

select * 
from sales.customers

# COMANDO DISTINCT

-- serve para remover linhas duplicadas e mostrar linhas distintas
-- muito utilizado na etapa de exploração dos dados

-- sintaxe
select distinct coluna_1, coluna_2 coluna_3
from schema_1.tabela_1

-- (exemplo 1) Seleção de uma coluna sem o distinct
- Liste as marcas de carro que constam na tabela products

select brand 
from sales.products

-- (exemplo 2) Seleção de uma coluna sem o distinct
- Liste as marcas de carros distintas

select distinct brand
from sales.products

-- (exemplo 3) Seleção de mais uma coluna sem o distinct
- Liste as marcas de carros e anos de modelos distintas

select distinct brand, model_year
from sales.products

# COMANDO WHERE 

-- serve para filtrar as linhas de uma tebla de acordo com uma condição
-- (exemplo 1) Filtro com condição única
- Liste os e-mails dos clientes da nossa base que residem no estado de Santa Catarina

select email, state
from sales.customers 
where state = 'SC' -- sempre aspas simples.

select distinct state
from sales.customers

-- (exemplo 2) Filtro com mais de condição
- Liste os e-maisl dos clientes que residem em SC ou MS

select email, state
from sales.customers 
where state = 'SC' or state = 'MS'

-- (exemplo 3) Filtro com mais de condição com data
- Liste os e-maisl dos clientes que residem em SC ou MS e que tem mais de 30 anos

select email, state, birth_date
from sales.customers 
where (state = 'SC' or state = 'MS’) and birth_date < ‘1993–12-29’

select distinct birth_date
from sales.customers

# COMANDO ORDER BY

-- serve para ordenar a seleção de acordo com uma regra definida pelo usuário
— sintaxe 

select coluna_1, coluna_2, coluna_3
from schema_1, tabela_1
where condição_x=true
order by coluna_1

-- (exemplo 1) Ordenação de valores numéricos
- Liste os produtos da tabela products na ordem crescente com base no preço

Select *
From sales.products
Order by price

-- (exemplo 2) Ordenação de texto
-- Liste os estados distintos da tabela customers na ordem crescente

Select distinct state
From sales.customers
Order by state

# COMANDO LIMIT

-- serve para limitar o número de linhas da consulta
— sintaxe 

select coluna_1, coluna_2, coluna_3
from schema_1, tabela_1
where condição_x=true
order by coluna_1
Limit N

-- (exemplo 1) Seleção de N números de linhas usando LIMIT
- Liste as 10 primeiras linhas da tabela funnel

Select * 
From sales.funnel
Limit 10

-- (exemplo 2) Seleção de N números de linhas usando LIMIT e ORDER BY
- Liste as 10 primeiros produtos mais caros da tabela products

Select *
From sales.product
Order by price desc
Limit 10

# OPERADORES ARITIMÉTICOS

—servem para executar operações matemáticas

— tipos
— || -> adição de strings

-- (exemplo 1) Criação de uma coluna calculada
- Crie uma coluna contendo a idade do cliente da tabela customers

Select 
email, 
birth_date,
9current_date - birth_date) /365 as client_age
From sales.customers


Select 
email, 
birth_date,
(current_date - birth_date) /365 as “client age”
From sales.customers

-- (exemplo 2) Criação de uma coluna calculada na query
- Crie uma coluna contendo os 10 clientes mais novos da tabela customers

Select 
email, 
birth_date,
(current_date - birth_date) /365 as client_age
From sales.customers
Order by client_age
Limit 10

-- (exemplo 3) Criação de uma coluna calculada com strings
-- Crie uma coluna “nome_completo” contendo o nome completo do cliente

Select 
	first_name || ’ ’ || last_name as full_name
From sales.customers

# OPERADORES COMPARAÇÃO

— servem para compar dosi valores retornando **TRUE e FALSE**
— muito utilizado em conjunto com a função WHERE para filtrar linhas de uma seleção

— tipos
= igual
> maior
< menor 
<= menor igual
>= maior igual
<> diferente 

