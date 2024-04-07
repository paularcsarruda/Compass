CREATE VIEW dim_Cliente AS
SELECT idCliente, 
       nomeCliente, 
       cidadeCliente, 
       estadoCliente, 
       paisCliente
FROM Cliente;

CREATE VIEW dim_Carro AS
SELECT idCarro,
       marcaCarro, 
       modeloCarro, 
       anoCarro, 
       idCombustivel
FROM Carro;

CREATE VIEW dim_Vendedor AS
SELECT idVendedor, 
       nomeVendedor, 
       sexoVendedor, 
       estadoVendedor
FROM Vendedor;

CREATE VIEW dim_Combustivel AS
SELECT idCombustivel,
       tipoCombustivel
FROM Combustivel;

CREATE VIEW Fato_Locacao AS
SELECT 
    l.idLocacao, 
    c.idCliente,    
    ca.idCarro, 
    v.idVendedor,
    l.qtdDiaria,
    l.vlrDiaria, 
    l.dataEntrega, 
    l.horaEntrega
FROM Locacao l
    JOIN dim_Cliente c 
        ON l.idCliente = c.idCliente
    JOIN dim_Carro ca 
        ON l.idCarro = ca.idCarro
    JOIN dim_Vendedor v
        ON l.idVendedor = v.idVendedor;
