select 
    editora.codeditora as CodEditora, 
    editora.nome as NomeEditora, 
    count(editora.nome) as QuantidadeLivros
from editora

inner join livro on editora.codeditora = livro.editora

group by 
    editora.nome
order by 
    QuantidadeLivros desc
limit 5;