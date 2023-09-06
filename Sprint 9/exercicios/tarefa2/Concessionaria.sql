CREATE VIEW Dim_Cliente AS
SELECT 
    idCliente, 
    nomeCliente, 
    cidadeCliente, 
    estadoCliente, 
    paisCliente
FROM Cliente;

CREATE VIEW Dim_Carro AS
SELECT idCarro,
    marcaCarro, 
    modeloCarro, 
    anoCarro, 
    idCombustivel
FROM Carro;

CREATE VIEW Dim_Vendedor AS
SELECT idVendedor, 
    nomeVendedor, 
    sexoVendedor, 
    estadoVendedor
FROM Vendedor;

CREATE VIEW Dim_Data AS
SELECT data, DAY(data) AS dia, MONTH(data) AS mes, YEAR(data) AS ano,
       CASE
           WHEN MONTH(data) <= 3 THEN 1
           WHEN MONTH(data) <= 6 THEN 2
           WHEN MONTH(data) <= 9 THEN 3
           ELSE 4
       END AS trimestre,
       CASE
           WHEN MONTH(data) <= 6 THEN 1
           ELSE 2
       END AS semestre
FROM Locacao; 

CREATE VIEW Fato_Locacao AS
SELECT 
    l.idLocacao, 
    c.idCliente,    
    ca.idCarro, 
    v.idVendedor, 
    d.data, 
    l.qtdDiaria, 
    l.vlrDiaria, 
    l.dataEntrega, 
    l.horaEntrega
FROM Locacao l
    JOIN Dim_Cliente c 
        ON l.idCliente = c.idCliente
    JOIN Dim_Carro ca 
        ON l.idCarro = ca.idCarro
    JOIN Dim_Vendedor v
        ON l.idVendedor = v.idVendedor
    JOIN Dim_Data d 
        ON l.dataLocacao = d.data;
