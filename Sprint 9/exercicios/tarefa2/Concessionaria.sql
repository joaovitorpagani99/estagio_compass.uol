-- Create a view for Car information
CREATE VIEW vw_car_info AS
SELECT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel
FROM Carro;

-- Create a view for Vendor information
CREATE VIEW vw_vendor_info AS
SELECT idVendedor, nomeVendedor, estadoVendedor, sexoVendedor
FROM Vendedor;

CREATE VIEW vw_fuel_info AS
SELECT idCombustivel, tipoCombustivel
FROM Combustivel;

-- Create a view for Customer information
CREATE VIEW vw_customer_info AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Cliente;

-- Create a view for Rental information
CREATE VIEW vw_rental_info AS
SELECT
    L.idLocacao,
    C.*,
    CAR.*,
    V.*,
    F.tipoCombustivel,
    L.dataLocacao,
    L.horaLocacao,
    L.qtdDiaria,
    L.vlrDiaria,
    L.dataEntrega,
    L.horaEntrega
FROM Locacao L
JOIN Cliente C ON L.idCliente = C.idCliente
JOIN Carro CAR ON L.idCarro = CAR.idCarro
JOIN Vendedor V ON L.idVendedor = V.idVendedor
JOIN Combustivel F ON CAR.idCombustivel = F.idCombustivel;
