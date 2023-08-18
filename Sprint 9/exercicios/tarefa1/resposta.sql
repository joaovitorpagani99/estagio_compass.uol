CREATE VIEW dim_cliente AS
SELECT
    idCliente,
    nomeCliente AS NomeCliente,
    cidadeCliente AS CidadeCliente,
    estadoCliente AS EstadoCliente,
    paisCliente AS PaisCliente
FROM Cliente;

CREATE VIEW dim_carro AS
SELECT
    idCarro,
    kmCarro,
    classiCarro AS ClassificacaoCarro,
    marcaCarro AS MarcaCarro,
    modeloCarro AS ModeloCarro,
    anoCarro AS AnoCarro
FROM Carro;

CREATE VIEW dim_combustivel AS
SELECT
    idCombustivel,
    tipoCombustivel
FROM Combustivel;

CREATE VIEW dim_vendedor AS
SELECT
    idVendedor AS idVendedor,
    nomeVendedor AS NomeVendedor,
    estadoVendedor AS EstadoVendedor,
    sexoVendedor AS SexoVendedor
FROM Vendedor;

CREATE VIEW fator_locacao AS
SELECT
    idLocacao,
    c.idCliente AS idCliente,
    ca.idCarro AS idCarro,
    dataLocacao AS DataLocacao,
    horaLocacao AS HoraLocacao,
    qtdDiaria AS QuantidadeDiaria,
    vlrDiaria AS ValorDiaria,
    dataEntrega AS DataEntrega,
    horaEntrega AS HoraEntrega,
    v.idVendedor AS idVendedor
FROM Locacao l
JOIN dim_cliente c ON l.idCliente = c.idCliente
JOIN dim_carro ca ON l.idCarro = ca.idCarro
JOIN dim_vendedor v ON l.idVendedor = v.idVendedor;
